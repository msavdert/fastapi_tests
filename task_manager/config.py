from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # API
    API_V1_PREFIX: str
    ENVIRONMENT: str

    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int
    AUTH_RATE_LIMIT_PER_MINUTE: int

    # HTTPS Configuration
    HTTPS_ENABLED: bool = False
    SSL_KEYFILE: Optional[str] = None
    SSL_CERTFILE: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings() 