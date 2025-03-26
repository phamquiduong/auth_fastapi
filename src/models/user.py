from typing import Sequence

from sqlmodel import Field, Session, SQLModel, select

from schemas.user import UserCreateSchema


class Users(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    email: str = Field(nullable=False, unique=True, index=True)
    password: str = Field(nullable=False)


class UserManager:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, offset: int, limit: int) -> Sequence[Users]:
        return self.session.exec(select(Users).offset(offset).limit(limit)).all()

    def get_by_email(self, email: str) -> Users | None:
        return self.session.exec(select(Users).where(Users.email == email)).one_or_none()

    def is_exist_email(self, email: str) -> bool:
        return self.session.exec(select(Users).where(Users.email == email)).first() is not None

    def create(self, user_create: UserCreateSchema) -> Users:
        user = Users(**user_create.model_dump(), password=user_create.hashed_password)
        self.session.add(user)
        self.session.flush()
        return user
