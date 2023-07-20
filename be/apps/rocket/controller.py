from typing import Dict, Optional

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from apps.container import Container
from apps.rocket.service import RocketService
from helpers.schemas.rocket.schema import (
    RockerPropertyCreateSchema,
    RocketNodeResponseSchema,
    RocketNodeSchema,
)

router = InferringRouter()


@cbv(router)
class RocketController:
    base_route = "Rocket"
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
        "/{route_path:path}",
        status_code=200,
    )
    async def get_tree(self, route_path: str) -> RocketNodeResponseSchema:
        result: RocketNodeSchema = await self.rocket_service.get_tree(
            route_path=route_path
        )
        return result

    @router.post(
        "/{route_path:path}",
        status_code=200,
    )
    async def create_node(
        self,
        route_path: str,
        rocket_property: Optional[RockerPropertyCreateSchema] = None,
    ) -> RocketNodeResponseSchema | Dict:
        result: RocketNodeSchema = await self.rocket_service.create(
            route_path=route_path, rocket_property=rocket_property
        )
        return result
