from fastapi import APIRouter, Body
from pydantic import EmailStr

from dependencies.database import SessionDependency
from exceptions.auth import PasswordIncorrectException
from exceptions.user import UserDoestNotExistException
from helpers import bcrypt, token
from models.user import UserManager
from schemas.api.login import LoginResponse
from schemas.token import AccessTokenSchema, RefreshTokenSchema
from settings import settings

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('login')
def authenticate_user(
    session: SessionDependency,
    email: EmailStr = Body(),
    password: str = Body(min_length=8)
) -> LoginResponse:
    user_manager = UserManager(session=session)
    user = user_manager.get_by_email(email=email)

    if not user:
        raise UserDoestNotExistException

    if not bcrypt.verify(plain_password=password, hashed_password=user.password):
        raise PasswordIncorrectException

    access_token_data = AccessTokenSchema(
        user_id=user.id,    # type:ignore
    )
    refresh_token_data = RefreshTokenSchema(
        user_id=user.id,    # type:ignore
    )

    return LoginResponse(
        access_token=token.create(data=access_token_data, expires_delta=settings.ACCESS_TOKEN_EXP),
        refresh_token=token.create(data=refresh_token_data, expires_delta=settings.REFRESH_TOKEN_EXP),
    )
