from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    email: EmailStr
    password: str


class UserCreateSchema(BaseModel):
    email: EmailStr
    hashed_password: str


class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str


class UserResponseSchema(BaseModel):
    id: int
    email: EmailStr
