from datetime import timedelta

from pydantic import BaseModel


class Settings(BaseModel):
    DATABASE_URL: str = "sqlite:///../db.sqlite3"

    SECRET_KEY: str = 'ndpI3qCRtFzz9rVIJ6n48zmQT3yHQqqU'    # Will read from enviroment
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXP: timedelta = timedelta(minutes=5)
    REFRESH_TOKEN_EXP: timedelta = timedelta(days=60)

    ORIGINS: list[str] = ['*']


settings = Settings()
