from typing import List, Optional, Tuple, Type

from pydantic import BaseModel
from sqlalchemy import and_, delete, select

from helpers.entity.sql_engine import async_session
from helpers.entity.sql_entity import SqlEntity
from helpers.models.non_flat_attrs import Node, Property
from helpers.schemas.non_flat_attrs.schema import NonFlatAttrsPropertyCreateSchema
from settings.base import Settings

from .entity import NonFlatAttrsFactory


class NonFlatAttrsRepository:
    def __init__(
        self,
        model: SqlEntity,
        factory: NonFlatAttrsFactory,
        schema: Type[BaseModel],
        config: Settings,
    ) -> None:
        self.model = model
        self.factory = factory
        self.schema = schema
        self.config = config

    async def get_property_by_latest_node_id(
        self, latest_node_id: int, property_name: str
    ) -> Optional[Property]:
        async with async_session() as session:
            result = await session.execute(
                select(Property).filter(
                    and_(
                        Property.node_id == latest_node_id,
                        Property.name == property_name,
                    )
                )
            )
            result = result.scalar_one_or_none()
            return result

    async def get_latest_node_id(
        self, path: List[str]
    ) -> Optional[Tuple[int, int, int]]:
        async with async_session() as session:
            result = True
            latest_node_id = None
            latest_node_steps = 0
            for index, node_name in enumerate(path):
                if index == 0:
                    result = await session.execute(
                        select(Node).filter(Node.name == node_name)
                    )
                    result = result.scalar_one_or_none()
                else:
                    result = await session.execute(
                        select(Node).filter(
                            and_(
                                Node.name == node_name,
                                Node.parent_id == result.id if result else None,
                            )
                        )
                    )
                    result = result.scalar_one_or_none()
                if result is not None:
                    latest_node_id = result.id
                else:
                    latest_node_steps += 1
            return result.id if result else None, latest_node_id, latest_node_steps

    @staticmethod
    async def get_node_list_by_node_id(node_id: int):
        async with async_session() as session:
            topq = (
                session.sync_session.query(Node, Property)
                .outerjoin(Property, Property.node_id == Node.id)
                .filter(Node.id == node_id)
                .order_by(Property.node_id)
                .cte("cte", recursive=True)
            )

            bottomq = (
                session.sync_session.query(Node, Property)
                .outerjoin(Property, Property.node_id == Node.id)
                .join(topq, Node.parent_id == topq.c.id)
                .order_by(Property.node_id)
            )
            recursive_q = topq.union(bottomq)
            q = session.sync_session.query(recursive_q)
            result = await session.execute(q)
            result = result.all()
            return result

    async def create_node(self, parent_node_id: int, name: str) -> Node:
        async with async_session() as session:
            new_node = Node(parent_id=parent_node_id, name=name)
            session.add(new_node)
            await session.commit()
            await session.refresh(new_node)
        return new_node

    async def create_property(
        self, parent_node_id: int, property: NonFlatAttrsPropertyCreateSchema
    ) -> Tuple[Node, Property]:
        async with async_session() as session:
            new_property = Property(
                node_id=parent_node_id,
                name=property.name,
                value=property.value,
            )
            session.add(new_property)
            await session.commit()
            await session.refresh(new_property)
            node = await session.execute(select(Node).filter(Node.id == parent_node_id))
            node = node.scalar()
        return node, new_property

    async def delete_node(self, node_id_list: List[int]) -> bool:
        async with async_session() as session:
            await session.execute(delete(Node).where(Node.id.in_(node_id_list)))
            await session.commit()
            return True

    async def delete_property(self, property_id_list: List[int]) -> bool:
        async with async_session() as session:
            await session.execute(
                delete(Property).where(Property.id.in_(property_id_list))
            )
            await session.commit()
            return True
