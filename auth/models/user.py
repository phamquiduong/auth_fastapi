from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    email: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)
