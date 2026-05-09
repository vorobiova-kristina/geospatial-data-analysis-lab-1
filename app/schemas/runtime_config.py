from dataclasses import dataclass
from typing import Literal, Optional

from pydantic import BaseModel, Field


class RuntimeConfigModel(BaseModel):
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    feature_flag: bool = False
    maintenance_mode: bool = False
    runtime_message: str = "Приложение работает в штатном режиме"


@dataclass
class RuntimeConfigUpdateModel(BaseModel):
    log_level: Optional[Literal["DEBUG", "INFO", "WARNING", "ERROR"]] = Field(None)
    feature_flag: Optional[bool] = Field(None)
    maintenance_mode: Optional[bool] = Field(None)
    runtime_message: Optional[str] = Field(None)
