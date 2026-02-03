from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvSettings (BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    pydantic_ai_gateway_api_key: str