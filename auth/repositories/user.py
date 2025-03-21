from typing import Literal

from sqlmodel import Session, select

import models
from schemas import user as user_schemas


class User:
    model = models.Users
    schema = user_schemas.User

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self, offset: int = 0, limit: int = 10) -> list[user_schemas.User]:
        users = self.session.exec(select(self.model).offset(offset).limit(limit)).all()
        return [self.schema(**user.__dict__) for user in users]

    def get_by_id(self, user_id: int) -> user_schemas.User | None:
        user = self.session.exec(select(self.model).where(self.model.id == user_id)).first()
        if user is not None:
            return self.schema(**user.__dict__)

    def get_by_email(self, email: str) -> user_schemas.User | None:
        user = self.session.exec(select(self.model).where(self.model.email == email)).first()
        if user is not None:
            return self.schema(**user.__dict__)

    def create(self, user_create_schema: user_schemas.Create) -> user_schemas.User:
        user = models.Users(
            id=None,
            email=user_create_schema.email,
            password=user_create_schema.hashed_password
        )

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return self.schema(**user.__dict__)

    def delete(self, user_id: int) -> Literal[True] | None:
        user = self.get_by_id(user_id)

        if user is None:
            user = self.session.delete(user)
            self.session.delete(user)
            self.session.commit()
            return True
