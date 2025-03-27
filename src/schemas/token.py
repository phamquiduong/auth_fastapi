from pydantic import BaseModel


class TokenSchema(BaseModel):
    token_type: str
    user_id: int


class AccessTokenSchema(TokenSchema):
    token_type: str = 'Access'


class RefreshTokenSchema(TokenSchema):
    token_type: str = 'Refresh'
