import os


class ApiConfig:
    def __init__(self):
        self.name = os.environ.get("APP_NAME", "newAPI")
        self.version = os.environ.get("APP_VERSION", "1.0.0")
        self.description = os.environ.get("APP_DESCRIPTION", "lab5")
        self.authors = os.environ.get("APP_AUTHORS", "Kristina Vorobeva")

    def get_static(self):
        return {
            "APP_NAME": self.name,
            "APP_VERSION": self.version,
            "APP_DESCRIPTION": self.description,
            "APP_AUTHORS": [self.authors],
        }


class RuntimeSettings:
    def __init__(self):
        self.log_level = "INFO"
        self.feature_flag = False
        self.maintenance_mode = False
        self.runtime_message = "Обычный режим работы"


app_config = ApiConfig()
