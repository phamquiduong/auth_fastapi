from fastapi import HTTPException, status

import helpers
import repositories
from schemas import user as user_schemas


class User:
    def __init__(self, repository: repositories.User):
        self.repository = repository

    def register(self, user_register: user_schemas.Register):
        if self.repository.get_by_email(email=user_register.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')

        bcrypt_helper = helpers.Bcrypt()
        hashed_password = bcrypt_helper.get_password_hash(user_register.password)

        user_create = user_schemas.Create(
            **user_register.model_dump(),
            hashed_password=hashed_password
        )

        return self.repository.create(user_create)

    def get_all(self, offset: int, limit: int):
        return self.repository.get_all(offset=offset, limit=limit)
