from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DB_DSN: PostgresDsn

    class Config:
        case_sensitive = True
        env_file = ".env"
