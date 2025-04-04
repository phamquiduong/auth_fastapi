from datetime import datetime, timedelta, timezone

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from pydantic import BaseModel

from exceptions import TokenExpiredException, TokenInvalidException
from helpers.json_ import JSONEncoder
from schemas.token import TokenSchema
from settings import settings


def create(data: dict | BaseModel, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy() if isinstance(data, dict) else data.model_dump()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(payload=to_encode, key=settings.SECRET_KEY,
                             algorithm=settings.ALGORITHM, json_encoder=JSONEncoder)
    return encoded_jwt


def decode(token: str) -> dict:
    return jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM])


def get_token_data(token: str) -> TokenSchema:
    try:
        payload = decode(token=token)
        token_data = TokenSchema(**payload)
    except ExpiredSignatureError as expired_exc:
        raise TokenExpiredException from expired_exc
    except InvalidTokenError as invalid_exc:
        raise TokenInvalidException from invalid_exc

    return token_data
