from pydantic import BaseModel


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
