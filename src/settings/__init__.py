from datetime import timedelta

from pydantic import BaseModel


class Settings(BaseModel):
    DATABASE_URL: str = "sqlite:///../db.sqlite3"

    SECRET_KEY: str = 'Insecurity'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXP: timedelta = timedelta(minutes=5)
    REFRESH_TOKEN_EXP: timedelta = timedelta(days=60)


settings = Settings()
