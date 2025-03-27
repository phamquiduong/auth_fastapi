from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr

from dependencies.database import SessionDependency
from exceptions.auth import PasswordIncorrectException
from exceptions.user import UserDoestNotExistException
from helpers import bcrypt, jwt_
from models.user import UserManager
from schemas.api.login import LoginResponse
from schemas.token import AccessTokenSchema, FastAPITokenResponse, RefreshTokenSchema
from settings import settings

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('/login')
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
        access_token=jwt_.create(data=access_token_data, expires_delta=settings.ACCESS_TOKEN_EXP),
        refresh_token=jwt_.create(data=refresh_token_data, expires_delta=settings.REFRESH_TOKEN_EXP),
    )


@auth_router.post("/token", include_in_schema=False)
async def login_for_access_token(
    session: SessionDependency,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> FastAPITokenResponse:
    user_manager = UserManager(session=session)
    user = user_manager.get_by_email(email=form_data.username)

    if not user:
        raise UserDoestNotExistException

    if not bcrypt.verify(plain_password=form_data.password, hashed_password=user.password):
        raise PasswordIncorrectException

    access_token_data = AccessTokenSchema(
        user_id=user.id,    # type:ignore
    )

    return FastAPITokenResponse(
        access_token=jwt_.create(data=access_token_data, expires_delta=settings.ACCESS_TOKEN_EXP),
        token_type="bearer"
    )
