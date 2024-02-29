from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encode = "utf-8"


settings = Settings()
