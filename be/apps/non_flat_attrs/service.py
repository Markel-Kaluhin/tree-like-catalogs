from typing import List

from helpers.exceptions.base import NonFlatAttrsException
from helpers.schemas.non_flat_attrs.schema import (
    NonFlatAttrsPropertyCreateSchema,
    NonFlatAttrsPropertySchema,
    NonFlatAttrsNodeSchema,
)

from .repository import NonFlatAttrsRepository


class NonFlatAttrsService:
    def __init__(self, repository: NonFlatAttrsRepository) -> None:
        self.repository = repository

    async def get_tree(self, route_path: str) -> NonFlatAttrsNodeSchema:
        path = self.__get_path(route_path=route_path)
        node_id, latest_node_id, _ = await self.repository.get_latest_node_id(path)
        non_flat_attrs_property = await self.repository.get_property_by_latest_node_id(
            latest_node_id, path[-1]
        )
        if node_id is None and non_flat_attrs_property is None:
            raise NonFlatAttrsException(
                custom_message="Node or property does not exist in this path"
            )
        node_list = await self.repository.get_node_list_by_node_id(latest_node_id)
        result = self.repository.factory.serialize(node_list, non_flat_attrs_property, path)
        return result

    async def create(
        self, route_path: str, non_flat_attrs_property: NonFlatAttrsPropertyCreateSchema
    ) -> NonFlatAttrsNodeSchema:
        path = self.__get_path(route_path=route_path)
        _, latest_node_id, latest_node_steps = await self.repository.get_latest_node_id(
            path
        )
        if latest_node_steps == 0:
            if non_flat_attrs_property is None:
                raise NonFlatAttrsException(custom_message="Node already exists")
        elif latest_node_steps > 1:
            raise NonFlatAttrsException(
                custom_message=f"Unable to create Node or Property, you specified a path containing "
                f"more than one non-existent node. First create the previous "
                f"{latest_node_steps - 1} "
                f"node{'s' if (latest_node_steps - 1) > 1 else ''} of this branch"
            )
        if non_flat_attrs_property is None:
            new_node = await self.repository.create_node(latest_node_id, path[-1])
            result = NonFlatAttrsNodeSchema.from_orm(new_node)
        else:
            node, new_property = await self.repository.create_property(
                latest_node_id, non_flat_attrs_property
            )
            new_property = NonFlatAttrsPropertySchema.from_orm(new_property)
            result = NonFlatAttrsNodeSchema.from_orm(node)
            result.properties.append(new_property)
        return result

    async def delete_node(self, node_id: int):
        node_list = await self.repository.get_node_list_by_node_id(node_id)
        property_id_list = list(set(i[5] for i in node_list if i[5] is not None))
        node_id_list = list(set(i[0] for i in node_list))
        await self.repository.delete_property(property_id_list=property_id_list)
        return await self.repository.delete_node(node_id_list=node_id_list)

    async def delete_property(self, property_id: int):
        return await self.repository.delete_property(property_id_list=[property_id])

    def __get_path(self, route_path: str) -> List[str]:
        return [i for i in route_path.split("/") if i != ""]
