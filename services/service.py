from config import RuntimeSettings


class RuntimeService:
    def __init__(self):
        self.runtime_settings = RuntimeSettings()

    def get_runtime(self):
        return vars(self.runtime_settings)

    def update_runtime(self, data: dict):
        for key, value in data.items():
            if hasattr(self.runtime_settings, key):
                setattr(self.runtime_settings, key, value)
        return self.get_runtime()


runtime_service = RuntimeService()
