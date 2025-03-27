from typing import Annotated

from fastapi import Depends
from jwt import ExpiredSignatureError, InvalidTokenError

from constants import TokenType
from dependencies.database import SessionDependency
from exceptions import (TokenExpiredException, TokenInvalidException, TokenTypeIncorrectException,
                        UserDoestNotExistException)
from helpers import jwt_
from models import UserManager, Users
from schemas.token import TokenSchema, oauth2_scheme


async def get_current_user(session: SessionDependency, token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt_.decode(token=token)
        token_data = TokenSchema(**payload)
    except ExpiredSignatureError as expired_exc:
        raise TokenExpiredException from expired_exc
    except InvalidTokenError as invalid_exc:
        raise TokenInvalidException from invalid_exc

    if token_data.token_type != TokenType.ACCESS:
        raise TokenTypeIncorrectException

    user_manager = UserManager(session=session)
    user = user_manager.get_by_id(user_id=token_data.user_id)

    if user is None:
        raise UserDoestNotExistException

    return user


CurrentUserDependency = Annotated[Users, Depends(get_current_user)]
