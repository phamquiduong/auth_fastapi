from fastapi import FastAPI

import repositories
import services
from dependencies.database import SessionDep
from schemas import user as user_schemas

app = FastAPI()


@app.post('/register/', response_model=user_schemas.Response)
async def register(user_register: user_schemas.Register, session: SessionDep):
    user_repository = repositories.User(session=session)
    user_service = services.User(repository=user_repository)
    return user_service.register(user_register=user_register).model_dump()
