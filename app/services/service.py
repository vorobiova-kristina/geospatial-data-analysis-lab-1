from app.schemas.runtime_config import (
    RuntimeConfigModel,
    RuntimeConfigUpdateModel,
)


class RuntimeConfigService:
    def __init__(self, initial_config: RuntimeConfigModel):
        self._config = initial_config.model_copy(deep=True)

    def get_config(self) -> RuntimeConfigModel:
        return self._config

    def update_config(
        self,
        new_config: RuntimeConfigUpdateModel,
    ) -> RuntimeConfigModel:
        current_data = self._config.model_dump()
        update_data = new_config.model_dump(exclude_unset=True)
        current_data.update(update_data)
        self._config = RuntimeConfigModel(**current_data)
        return self._config
