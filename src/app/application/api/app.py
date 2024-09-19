from fastapi import FastAPI

from ...logic.containers import LogicContainer
from .v1.router import router as v1_router


def create_app() -> FastAPI:
    container = LogicContainer()

    app = FastAPI(
        title="FastAPI MongoDB Simple Example",
        docs_url="/api/docs",
    )
    app.container = container

    app.include_router(
        v1_router,
        prefix="/api/v1",
    )
    return app
