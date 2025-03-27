from fastapi import APIRouter, Body, Query
from pydantic import EmailStr

from dependencies.database import SessionDependency
from exceptions.user import UserAlreadyExistsException
from helpers import bcrypt
from models.user import UserManager
from schemas.user import UserCreateSchema, UserResponse

user_router = APIRouter(prefix='/users', tags=['User'])


@user_router.get('/')
async def get_all_users(
    session: SessionDependency,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, le=10),
) -> list[UserResponse]:
    user_manager = UserManager(session=session)

    users = user_manager.get_all(offset=offset, limit=limit)
    return [UserResponse(**user.model_dump()) for user in users]


@user_router.post('/register')
async def register(
    session: SessionDependency,
    email: EmailStr = Body(),
    password: str = Body(min_length=8)
) -> UserResponse:
    user_manager = UserManager(session=session)

    if user_manager.is_exist_email(email=email) is True:
        raise UserAlreadyExistsException

    hashed_password = bcrypt.get_hash(password=password)
    user_create = UserCreateSchema(email=email, hashed_password=hashed_password)

    user = user_manager.create(user_create)

    return UserResponse(**user.model_dump())
