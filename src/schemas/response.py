from pydantic import BaseModel


class ErrorField(BaseModel):
    name: str
    errors: list[str]


class ErrorResponseSchema(BaseModel):
    status: int
    message: str
    error_code: str
    error_fields: list[ErrorField] | None = None
