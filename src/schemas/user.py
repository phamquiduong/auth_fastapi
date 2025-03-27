from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    id: int
    email: EmailStr
    role: str


class UserSchema(UserBase):
    password: str


class UserCreateSchema(BaseModel):
    email: EmailStr
    hashed_password: str


class UserResponse(UserBase):
    ...
