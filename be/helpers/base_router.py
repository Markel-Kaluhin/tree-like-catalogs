from typing import Any

from fastapi import FastAPI


def register_routes(
    fast_app: FastAPI,
    app: Any,
    root_url_tag: str = "api",
) -> None:
    fast_app.include_router(
        app.router, prefix=f"/{root_url_tag}/{app.base_route}", tags=app.tags
    )
