from fastapi import APIRouter, Query

from dependencies.database import SessionDependency
from exceptions.user import UserAlreadyExistsException
from helpers import bcrypt as bcrypt_helper
from models.user import UserManager
from schemas.user import UserCreateSchema, UserRegisterSchema, UserResponseSchema

user_router = APIRouter(prefix='/users')


@user_router.get('/')
async def get_all_users(
    session: SessionDependency,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, le=10),
) -> list[UserResponseSchema]:
    user_manager = UserManager(session=session)

    users = user_manager.get_all(offset=offset, limit=limit)
    return [UserResponseSchema(**user.model_dump()) for user in users]


@user_router.post('/register')
async def register(
    session: SessionDependency,
    user_register: UserRegisterSchema,
) -> UserResponseSchema:
    user_manager = UserManager(session=session)

    if user_manager.is_exist_email(email=user_register.email) is True:
        raise UserAlreadyExistsException

    hashed_password = bcrypt_helper.get_password_hash(password=user_register.password)
    user_create = UserCreateSchema(**user_register.model_dump(), hashed_password=hashed_password)

    user = user_manager.create(user_create)

    return UserResponseSchema(**user.model_dump())
