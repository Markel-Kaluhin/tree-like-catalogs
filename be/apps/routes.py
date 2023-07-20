from fastapi import FastAPI

from apps.rocket.controller import RocketController
from helpers.base_router import register_routes


def register_all_routes(fast_app: FastAPI) -> None:
    register_routes(fast_app, RocketController)
