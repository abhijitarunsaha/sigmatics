from __future__ import annotations

from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class ApplicationSettings(BaseModel):
    """
    General application configuration.
    """

    name: str
    version: str
    
class LogSettings(BaseModel):
    """
    Logging configuration.
    """

    log_level: str = "INFO"


class KiteSettings(BaseModel):
    """
    Zerodha Kite configuration.
    """

    api_key: str
    api_secret: str
    redirect_url: str
    access_token: str = ""


class SupabaseSettings(BaseModel):
    """
    Supabase configuration.
    """

    url: str = ""
    key: str = ""


class OpenAISettings(BaseModel):
    """
    OpenAI configuration.
    """

    api_key: str = ""


class Settings(BaseSettings):
    """
    Central application configuration.

    Loaded from the project's .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    #
    # Raw environment variables
    #

    APP_NAME: str = "Sigmatics"
    APP_VERSION: str = "0.1.0"
    
    LOG_LEVEL: str

    KITE_API_KEY: str
    KITE_API_SECRET: str
    KITE_REDIRECT_URL: str
    KITE_ACCESS_TOKEN: str = ""

    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    OPENAI_API_KEY: str = ""

    @property
    def app(self) -> ApplicationSettings:

        return ApplicationSettings(
            name=self.APP_NAME,
            version=self.APP_VERSION,
        )
        
    @property
    def log(self) -> LogSettings:

        return LogSettings(
            log_level=self.LOG_LEVEL,
        )

    @property
    def kite(self) -> KiteSettings:

        return KiteSettings(
            api_key=self.KITE_API_KEY,
            api_secret=self.KITE_API_SECRET,
            redirect_url=self.KITE_REDIRECT_URL,
            access_token=self.KITE_ACCESS_TOKEN,
        )

    @property
    def supabase(self) -> SupabaseSettings:

        return SupabaseSettings(
            url=self.SUPABASE_URL,
            key=self.SUPABASE_KEY,
        )

    @property
    def openai(self) -> OpenAISettings:

        return OpenAISettings(
            api_key=self.OPENAI_API_KEY,
        )


@lru_cache
def get_settings() -> Settings:
    """
    Returns the singleton application settings.
    """

    return Settings()