from pydantic import BaseModel


class Settings(BaseModel):
    database_url: str = "sqlite:///../db.sqlite3"


settings = Settings()
