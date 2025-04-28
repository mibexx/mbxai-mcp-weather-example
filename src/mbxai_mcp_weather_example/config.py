import importlib.metadata
import logging
from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent.parent.parent
SERVICE_NAME = "MBXAI_MCP_WEATHER_EXAMPLE_"


def _get_version() -> str:
    """Get the package version."""
    try:
        return importlib.metadata.version("mbxai_mcp_weather_example")
    except importlib.metadata.PackageNotFoundError:
        return "0.1.0"  # Default during development


class ApplicationConfig(BaseSettings):
    """Application configuration."""

    name: str = "MBXAI Mcp Weather Example"
    version: str = Field(default_factory=_get_version)
    log_level: int = logging.INFO

    model_config = SettingsConfigDict(
        env_prefix=SERVICE_NAME,
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache
def get_config() -> ApplicationConfig:
    """Get the application configuration singleton."""
    return ApplicationConfig()