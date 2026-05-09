import os

from app.schemas.app_config import AppConfigModel

app_config = AppConfigModel(
    name=os.environ.get("APP_NAME", "newAPI"),
    version=os.environ.get("APP_VERSION", "1.0.0"),
    description=os.environ.get("APP_DESCRIPTION", "lab5"),
    authors=[os.environ.get("APP_AUTHORS", "Kristina Vorobeva")],
)
