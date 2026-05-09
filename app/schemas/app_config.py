from pydantic import BaseModel, Field


class AppConfigModel(BaseModel):
    name: str = Field(default="newAPI", description="name of the API")
    version: str = Field(default="1.0.0", description="version of the API")
    description: str = Field(default="lab6", description="description of the API")
    authors: list[str] = Field(
        default="Kristina Vorobeva", description="authors of the API"
    )
