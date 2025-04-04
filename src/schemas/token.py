import uuid

from fastapi.security import OAuth2PasswordBearer
from pydantic import UUID4, BaseModel, Field


class TokenSchema(BaseModel):
    jta: UUID4 = Field(default_factory=uuid.uuid4)
    token_type: str
    user_id: int


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class FastAPITokenResponse(BaseModel):
    access_token: str
    token_type: str
