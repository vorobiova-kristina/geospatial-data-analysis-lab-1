import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.dependencies import get_app_config
from app.init_dependencies import init_dependencies
from app.routers.routers import router as config_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    deps = init_dependencies()
    app.state.deps = deps
    print(deps)
    yield
    print("App is shut down")


app = FastAPI(
    lifespan=lifespan,
    title=os.environ.get("APP_NAME", "newAPI"),
    description=os.environ.get("APP_DESCRIPTION", "lab6"),
    version=os.environ.get("APP_VERSION", "1.0.0"),
    contact={"name": os.environ.get("APP_AUTHORS", "Kristina Vorobeva")},
)


@app.get("/")
async def get_root():
    return RedirectResponse("/docs")


@app.get("/ping")
async def ping_server():
    return "pong"


app.include_router(config_router)
