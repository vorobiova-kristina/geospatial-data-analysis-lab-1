from fastapi import APIRouter

from config import app_config
from services.service import runtime_service

router = APIRouter()


@router.get("/config/app")
async def get_static_config():
    return app_config.get_static()


@router.get("/config/runtime")
async def get_runtime_config():
    return runtime_service.get_runtime()


@router.put("/config/runtime")
async def update_runtime_config(new_params: dict):
    return runtime_service.update_runtime(new_params)
