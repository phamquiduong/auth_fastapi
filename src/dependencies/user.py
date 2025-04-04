from typing import Annotated

from fastapi import Depends

from constants import TokenType
from dependencies.database import SessionDependency
from exceptions import TokenTypeIncorrectException, UserDoestNotExistException
from helpers import jwt_
from models import UserManager, Users
from schemas.token import oauth2_scheme


async def get_current_user(session: SessionDependency, token: Annotated[str, Depends(oauth2_scheme)]):
    token_data = jwt_.get_token_data(token=token)

    if token_data.token_type != TokenType.ACCESS:
        raise TokenTypeIncorrectException

    user_manager = UserManager(session=session)
    user = user_manager.get_by_id(user_id=token_data.user_id)

    if user is None:
        raise UserDoestNotExistException

    return user


CurrentUserDependency = Annotated[Users, Depends(get_current_user)]
