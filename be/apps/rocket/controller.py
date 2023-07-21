from typing import Optional

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from apps.container import Container
from apps.rocket.service import RocketService
from helpers.schemas.rocket.schema import RockerPropertyCreateSchema, RocketNodeSchema

router = InferringRouter()


@cbv(router)
class RocketController:
    base_route = "rocket"
    tags = ["Rocket"]
    router = router

    @inject
    def __init__(
        self,
        rocket_service: RocketService = Depends(
            Provide[Container.rocket_package.rocket_service]
        ),
    ):
        self.rocket_service = rocket_service

    @router.get(
        "/construction/{route_path:path}",
        status_code=200,
    )
    async def get_tree(self, route_path: str) -> RocketNodeSchema:
        result: RocketNodeSchema = await self.rocket_service.get_tree(
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
        rocket_property: Optional[RockerPropertyCreateSchema] = None,
    ) -> RocketNodeSchema:
        result: RocketNodeSchema = await self.rocket_service.create(
            route_path=route_path, rocket_property=rocket_property
        )
        return result

    @router.delete(
        "/node/{node_id}",
        status_code=200,
    )
    async def delete_node(self, node_id: int) -> bool:
        result: bool = await self.rocket_service.delete_node(node_id=node_id)
        return result

    @router.delete(
        "/property/{property_id}",
        status_code=200,
    )
    async def delete_property(self, property_id: int) -> bool:
        result: bool = await self.rocket_service.delete_property(
            property_id=property_id
        )
        return result
