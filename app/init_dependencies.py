from typing import Any

from app.config import app_config
from app.schemas.app_config import AppConfigModel
from app.schemas.runtime_config import RuntimeConfigModel
from app.services.service import RuntimeConfigService


class DependencyContainer(dict):
    def get_dependency(self, key: str) -> Any:
        if key not in self:
            raise KeyError(f"Dependency '{key}' not found in container")
        return self.get(key)


def init_dependencies() -> DependencyContainer:
    runtime_service = RuntimeConfigService(RuntimeConfigModel())
    container = DependencyContainer(
        {"app_config": app_config, "runtime_config_service": runtime_service}
    )
    return container
