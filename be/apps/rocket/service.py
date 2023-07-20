from typing import List

from helpers.exceptions.base import RocketException
from helpers.schemas.rocket.schema import (
    RockerPropertyCreateSchema,
    RockerPropertySchema,
    RocketNodeSchema,
)

from .repository import RocketRepository


class RocketService:
    def __init__(self, repository: RocketRepository) -> None:
        self.repository = repository

    async def get_tree(self, route_path: str) -> RocketNodeSchema:
        path = self.__get_path(route_path=route_path)
        node_id, latest_node_id, _ = await self.repository.get_latest_node_id(path)
        rocket_property = await self.repository.get_property_by_latest_node_id(
            latest_node_id, path[-1]
        )
        if node_id is None and rocket_property is None:
            raise RocketException(
                custom_message="Node or property does not exist in this path"
            )
        node_list = await self.repository.get_node_list_by_node_id(latest_node_id)
        result = self.repository.factory.serialize(node_list, rocket_property, path)
        return result

    async def create(
        self, route_path: str, rocket_property: RockerPropertyCreateSchema
    ) -> RocketNodeSchema:
        path = self.__get_path(route_path=route_path)
        _, latest_node_id, latest_node_steps = await self.repository.get_latest_node_id(
            path
        )
        if latest_node_steps == 0:
            if rocket_property is None:
                raise RocketException(custom_message="Node already exists")
        elif latest_node_steps > 1:
            raise RocketException(
                custom_message=f"Unable to create Node or Property, you specified a path containing "
                f"more than one non-existent node. First create the previous "
                f"{latest_node_steps - 1} "
                f"node{'s' if (latest_node_steps - 1) > 1 else ''} of this branch"
            )
        if rocket_property is None:
            new_node = await self.repository.create_node(latest_node_id, path[-1])
            result = RocketNodeSchema.from_orm(new_node)
        else:
            node, new_property = await self.repository.create_property(
                latest_node_id, rocket_property
            )
            new_property = RockerPropertySchema.from_orm(new_property)
            result = RocketNodeSchema.from_orm(node)
            result.properties.append(new_property)
        return result

    async def delete_node(self, node_id: int):
        node_id_list = list(set(i[0] for i in await self.repository.get_node_list_by_node_id(node_id)))
        return await self.repository.delete_node(node_id_list=node_id_list)

    async def delete_property(self, property_id: int):
        return await self.repository.delete_property(property_id=property_id)

    def __get_path(self, route_path: str) -> List[str]:
        return [i for i in route_path.split("/") if i != ""]
