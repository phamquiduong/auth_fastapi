from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from constants.token import TokenType


class TokenSchema(BaseModel):
    token_type: str
    user_id: int


class AccessTokenSchema(TokenSchema):
    token_type: str = TokenType.ACCESS


class RefreshTokenSchema(TokenSchema):
    token_type: str = TokenType.REFRESH


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class FastAPITokenResponse(BaseModel):
    access_token: str
    token_type: str
