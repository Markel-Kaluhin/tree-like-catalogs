from typing import List, Optional

from sqlalchemy.engine import Row

from helpers.models.non_flat_attrs import Property
from helpers.schemas.non_flat_attrs.schema import NonFlatAttrsPropertySchema, NonFlatAttrsNodeSchema


class NonFlatAttrsFactory:
    def serialize(
        self, non_flat_attrs_list: List[Row], non_flat_attrs_property: Property, path: List[str]
    ) -> NonFlatAttrsNodeSchema:
        path = path[:]
        for index, (
            node_id,
            parent_id,
            node_name,
            node_created_at,
            node_updated_at,
            property_id,
            non_flat_attrs_node_id,
            property_name,
            property_value,
            property_created_at,
            property_updated_at,
        ) in enumerate(non_flat_attrs_list):
            if index == 0:
                root = NonFlatAttrsNodeSchema(
                    id=node_id,
                    parent_id=parent_id,
                    name=node_name,
                    created_at=node_created_at,
                )
                properties = self.__get_properties(non_flat_attrs_list, non_flat_attrs_node_id)
                if non_flat_attrs_property:
                    properties = [
                        i for i in properties if i.name == non_flat_attrs_property.name
                    ]
                root.properties = properties
            else:
                parent_node = self.__get_parent_node(node=root, parent_id=parent_id)
                if parent_node is not None:
                    if non_flat_attrs_property:
                        if node_name in path:
                            path.pop(path.index(node_name))
                        else:
                            continue
                    node = NonFlatAttrsNodeSchema(
                        id=node_id,
                        parent_id=parent_id,
                        name=node_name,
                        created_at=node_created_at,
                    )
                    node.properties = self.__get_properties(non_flat_attrs_list, non_flat_attrs_node_id)
                    if node.id not in [i.id for i in parent_node.children]:
                        parent_node.children.append(node)
        return root

    def __get_properties(self, non_flat_attrs_list: List[Row], _non_flat_attrs_node_id: int):
        result = []
        for (
            _,
            _,
            _,
            _,
            _,
            property_id,
            non_flat_attrs_node_id,
            property_name,
            property_value,
            property_created_at,
            property_updated_at,
        ) in non_flat_attrs_list:
            if _non_flat_attrs_node_id is not None and non_flat_attrs_node_id == _non_flat_attrs_node_id:
                result.append(
                    NonFlatAttrsPropertySchema(
                        id=property_id,
                        name=property_name,
                        value=property_value,
                        created_at=property_created_at,
                    )
                )
        return result

    def __get_parent_node(
        self, node: NonFlatAttrsNodeSchema, parent_id: int
    ) -> Optional[NonFlatAttrsNodeSchema]:
        if node.id == parent_id:
            return node
        for child_node in node.children:
            result = self.__get_parent_node(child_node, parent_id)
            if result is None:
                continue
            return result
