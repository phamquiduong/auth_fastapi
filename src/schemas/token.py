from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel


class TokenSchema(BaseModel):
    token_type: str
    user_id: int


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


class FastAPITokenResponse(BaseModel):
    access_token: str
    token_type: str
