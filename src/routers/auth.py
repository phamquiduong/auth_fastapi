from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlmodel import Session

from constants.token import TokenType
from dependencies.database import SessionDependency
from exceptions.auth import PasswordIncorrectException
from exceptions.user import EmailDoestNotExistException
from helpers import bcrypt, jwt_
from models.user import UserManager, Users
from schemas.login import LoginResponseSchema
from schemas.token import FastAPITokenResponse, TokenSchema
from settings import settings

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


def get_user(session: Session, email: str, password: str) -> Users:
    user_manager = UserManager(session=session)
    user = user_manager.get_by_email(email=email)

    if not user:
        raise EmailDoestNotExistException

    if not bcrypt.verify(plain_password=password, hashed_password=user.password):
        raise PasswordIncorrectException

    return user


@auth_router.post('/login')
async def authenticate_user(
    session: SessionDependency,
    email: EmailStr = Body(),
    password: str = Body(min_length=8)
) -> LoginResponseSchema:
    user = get_user(session=session, email=email, password=password)

    access_token_data = TokenSchema(
        token_type=TokenType.ACCESS,
        user_id=user.id,    # type:ignore
    )
    refresh_token_data = TokenSchema(
        token_type=TokenType.REFRESH,
        user_id=user.id,    # type:ignore
    )

    return LoginResponseSchema(
        access_token=jwt_.create(data=access_token_data, expires_delta=settings.ACCESS_TOKEN_EXP),
        refresh_token=jwt_.create(data=refresh_token_data, expires_delta=settings.REFRESH_TOKEN_EXP),
    )


@auth_router.post("/token", include_in_schema=False)
async def login_for_access_token(
    session: SessionDependency,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> FastAPITokenResponse:
    user = get_user(session=session, email=form_data.username, password=form_data.password)

    access_token_data = TokenSchema(
        token_type=TokenType.ACCESS,
        user_id=user.id,    # type:ignore
    )

    return FastAPITokenResponse(
        access_token=jwt_.create(data=access_token_data, expires_delta=settings.ACCESS_TOKEN_EXP),
        token_type="bearer"
    )
