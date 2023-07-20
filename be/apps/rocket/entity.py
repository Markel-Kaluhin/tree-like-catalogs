from typing import List, Optional

from sqlalchemy.engine import Row

from helpers.models.rocket import RocketProperty
from helpers.schemas.rocket.schema import RockerPropertySchema, RocketNodeSchema


class RocketFactory:
    def serialize(
        self, rocket_list: List[Row], rocket_property: RocketProperty, path: List[str]
    ) -> RocketNodeSchema:
        path = path[:]
        for index, (
            node_id,
            parent_id,
            node_name,
            node_created_at,
            node_updated_at,
            property_id,
            rocket_node_id,
            property_name,
            property_value,
            property_created_at,
            property_updated_at,
        ) in enumerate(rocket_list):
            if index == 0:
                root = RocketNodeSchema(
                    id=node_id,
                    parent_id=parent_id,
                    name=node_name,
                    created_at=node_created_at,
                )
                properties = self.__get_properties(rocket_list, rocket_node_id)
                if rocket_property:
                    properties = [
                        i for i in properties if i.name == rocket_property.name
                    ]
                root.properties = properties
            else:
                parent_node = self.__get_parent_node(node=root, parent_id=parent_id)
                if parent_node is not None:
                    if rocket_property:
                        if node_name in path:
                            path.pop(path.index(node_name))
                        else:
                            continue
                    node = RocketNodeSchema(
                        id=node_id,
                        parent_id=parent_id,
                        name=node_name,
                        created_at=node_created_at,
                    )
                    node.properties = self.__get_properties(rocket_list, rocket_node_id)
                    if node.id not in [i.id for i in parent_node.children]:
                        parent_node.children.append(node)
        return root

    def __get_properties(self, rocket_list: List[Row], _rocket_node_id: int):
        result = []
        for (
            _,
            _,
            _,
            _,
            _,
            property_id,
            rocket_node_id,
            property_name,
            property_value,
            property_created_at,
            property_updated_at,
        ) in rocket_list:
            if _rocket_node_id is not None and rocket_node_id == _rocket_node_id:
                result.append(
                    RockerPropertySchema(
                        name=property_name,
                        value=property_value,
                        created_at=property_created_at,
                    )
                )
        return result

    def __get_parent_node(
        self, node: RocketNodeSchema, parent_id: int
    ) -> Optional[RocketNodeSchema]:
        if node.id == parent_id:
            return node
        for child_node in node.children:
            result = self.__get_parent_node(child_node, parent_id)
            if result is None:
                continue
            return result
