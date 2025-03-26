from schemas.response import ErrorField, ErrorResponseSchema


class APIException(Exception):
    def __init__(
        self,
        status: int,
        message: str,
        error_code: str | None = None,
        error_fields: dict[str, list[str] | str] | None = None
    ) -> None:
        self.status = status
        self.message = message
        self.error_code = error_code
        self.error_fields = error_fields

    def to_dict(self) -> dict:
        if not self.error_code:
            self.error_code = f'ERR-{self.status}-undefined'

        error_response = ErrorResponseSchema(
            status=self.status,
            message=self.message,
            error_code=self.error_code,
        )

        if self.error_fields:
            error_fields = [
                ErrorField(
                    name=field_name,
                    errors=errors if isinstance(errors, list) else [errors],
                )
                for field_name, errors in self.error_fields.items()
            ]
            error_response.error_fields = error_fields

        return error_response.model_dump(exclude_none=True)
