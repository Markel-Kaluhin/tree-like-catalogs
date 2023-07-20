from typing import Dict

import uvicorn
from dependency_injector.containers import Container
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from apps.routes import register_all_routes
from apps.wire import wire_container
from helpers.exceptions.base import BaseServiceException
from helpers.exceptions.middleware import (
    base_exception_handler,
    general_exception_handler,
)
from settings.base import settings


def create_app(container: Container) -> FastAPI:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=[settings.allow_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )
    ]
    fast_app = FastAPI(middleware=middleware)
    fast_app.container = container
    register_all_routes(fast_app)
    return fast_app


app = create_app(container=wire_container())

app.add_exception_handler(500, general_exception_handler)
app.add_exception_handler(422, general_exception_handler)
app.add_exception_handler(BaseServiceException, base_exception_handler)


@app.get("/health")
def health() -> Dict:
    return {"status": "healthy"}


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        port=settings.app_port,
        host=settings.app_host,
        log_level="debug",
        reload=settings.reload_app,
    )
