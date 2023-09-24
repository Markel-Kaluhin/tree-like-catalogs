from fastapi import FastAPI

from apps.non_flat_attrs.controller import NonFlatAttrsController
from helpers.base_router import register_routes


def register_all_routes(fast_app: FastAPI) -> None:
    register_routes(fast_app, NonFlatAttrsController)
