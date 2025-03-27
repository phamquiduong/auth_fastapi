from datetime import datetime, timedelta, timezone

import jwt
from pydantic import BaseModel

from settings import settings


def create(data: dict | BaseModel, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy() if isinstance(data, dict) else data.model_dump()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
