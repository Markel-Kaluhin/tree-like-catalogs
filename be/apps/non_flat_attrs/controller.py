from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from apps.container import Container
from apps.non_flat_attrs.service import NonFlatAttrsService
from helpers.schemas.non_flat_attrs.schema import NonFlatAttrsPropertyCreateSchema, NonFlatAttrsNodeSchema

router = InferringRouter()


@cbv(router)
class NonFlatAttrsController:
    base_route = "non_flat_attrs"
    tags = ["NonFlatAttrs"]
    router = router

    @inject
    def __init__(
        self,
        non_flat_attrs_service: NonFlatAttrsService = Depends(
            Provide[Container.non_flat_attrs_package.non_flat_attrs_service]
        ),
    ):
        self.non_flat_attrs_service = non_flat_attrs_service

    @router.get(
        "/construction/{route_path:path}",
        status_code=200,
    )
    async def get_tree(self, route_path: str) -> NonFlatAttrsNodeSchema:
        result: NonFlatAttrsNodeSchema = await self.non_flat_attrs_service.get_tree(
            route_path=route_path
        )
        return result

    @router.post(
        "/construction/{route_path:path}",
        status_code=200,
    )
    async def create_node(
        self,
        route_path: str,
        non_flat_attrs_property: Optional[NonFlatAttrsPropertyCreateSchema] = None,
    ) -> NonFlatAttrsNodeSchema:
        result: NonFlatAttrsNodeSchema = await self.non_flat_attrs_service.create(
            route_path=route_path, non_flat_attrs_property=non_flat_attrs_property
        )
        return result

    @router.delete(
        "/node/{node_id}",
        status_code=200,
    )
    async def delete_node(self, node_id: int) -> bool:
        result: bool = await self.non_flat_attrs_service.delete_node(node_id=node_id)
        return result

    @router.delete(
        "/property/{property_id}",
        status_code=200,
    )
    async def delete_property(self, property_id: int) -> bool:
        result: bool = await self.non_flat_attrs_service.delete_property(
            property_id=property_id
        )
        return result
