from pathlib import Path

from dotenv import find_dotenv
from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


BASE_DIR = Path(__file__).parent.parent


class RunSettings(BaseModel):
    scheme: str = "http"
    host: str = "0.0.0.0"
    port: int = 8000
    url: str = f"{scheme}://{host}:{port}"


class EmailSettings(BaseModel):
    login: str
    password: str


class DBSettings(BaseModel):
    user: str
    password: str
    host: str
    port: int
    name: str
    echo: bool

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=find_dotenv(".env"),
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="_",
    )
    db: DBSettings
    email: EmailSettings
    run: RunSettings = RunSettings()


settings = Settings()
