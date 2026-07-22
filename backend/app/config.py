"""Application configuration loaded from environment variables."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Default to a local SQLite file. In production set DATABASE_URL to a
    # Postgres connection string (Neon, Supabase, Railway, etc.).
    DATABASE_URL: str = "sqlite:///./campus_lost_found.db"

    # Secret used to sign JWT tokens. Override in production.
    JWT_SECRET: str = "change-me-in-production-please"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day

    # Comma separated list of allowed frontend origins for CORS.
    # "*" allows any origin, which is convenient for a first deploy. Tighten it
    # to your real frontend URL once that is known.
    CORS_ORIGINS: str = "*"

    class Config:
        env_file = ".env"


settings = Settings()
