from fastapi import APIRouter, Query

import repositories
import services
from dependencies.database import SessionDep
from schemas import user as user_schemas

router = APIRouter(prefix='/users')


@router.get('/')
async def get_all_users(
    session: SessionDep,
    offset: int = Query(0, ge=0),
    limit: int = Query(10, le=10),
) -> list[user_schemas.Response]:
    user_repository = repositories.User(session=session)
    user_service = services.User(repository=user_repository)

    users = user_service.get_all(offset=offset, limit=limit)
    return [user_schemas.Response(**user.model_dump()) for user in users]


@router.post('/register')
async def register(session: SessionDep, user_register: user_schemas.Register) -> user_schemas.Response:
    user_repository = repositories.User(session=session)
    user_service = services.User(repository=user_repository)

    user = user_service.register(user_register=user_register)
    return user_schemas.Response(**user.model_dump())
