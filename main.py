from fastapi import FastAPI

from config import app_config
from routers.routers import router

app = FastAPI(
    title=app_config.name,
    version=app_config.version,
    description=app_config.description,
    contact={"name": app_config.authors},
)


@app.get("/health")
async def get_health():
    return {"status": "ok"}


app.include_router(router)
