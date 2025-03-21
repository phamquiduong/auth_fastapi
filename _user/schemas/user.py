from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    password: str


class Create(BaseModel):
    email: EmailStr
    hashed_password: str


class Register(BaseModel):
    email: EmailStr
    password: str


class Response(BaseModel):
    id: int
    email: EmailStr
