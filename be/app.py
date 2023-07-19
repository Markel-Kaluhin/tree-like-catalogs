from typing import Dict

import uvicorn
from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


def create_app() -> FastAPI:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
            expose_headers=["*"],
        )
    ]
    fast_app = FastAPI(middleware=middleware)
    return fast_app


app = create_app()

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "healthy"}


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "app_service:app",
        host="0.0.0.0",
        port=80000,
        log_level="debug",
        reload=True,
    )
