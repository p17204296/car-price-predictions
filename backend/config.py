from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Car Price Predictions App"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class Settings(CommonSettings, ServerSettings):
    pass


settings = Settings()
