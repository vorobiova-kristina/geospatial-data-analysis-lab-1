from fastapi import Request

from app.schemas.app_config import AppConfigModel
from app.services.service import RuntimeConfigService


def get_system_service(request: Request):
    return request.app.state.deps


def get_app_config(request: Request) -> AppConfigModel:
    deps = get_system_service(request)
    return deps.get_dependency("app_config")


def get_runtime_config_service(request: Request) -> RuntimeConfigService:
    deps = get_system_service(request)
    return deps.get_dependency("runtime_config_service")
