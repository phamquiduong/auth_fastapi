from collections import defaultdict

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from exceptions.base import APIException


def handler_exception(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def request_validation_error_handler(_, exc: RequestValidationError):
        error_fields: dict[str, list[str]] = defaultdict(list)
        for error in exc.errors():
            loc, msg = error["loc"], error["msg"]
            loc = [item for item in loc if item not in (
                "body", "query", "path") and isinstance(item, str)] or ['__all__']
            for field_name in loc:
                error_fields[field_name].append(msg)

        api_exc = APIException(
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message='Request validation error',
            error_code='ERR-SYS-422-000',
            error_fields=error_fields,  # type:ignore
        )
        return JSONResponse(status_code=api_exc.status, content=api_exc.to_dict())

    @app.exception_handler(HTTPException)
    async def http_exception_handler(_, exc: HTTPException):
        api_exc = APIException(
            status=exc.status_code,
            message=exc.detail,
            error_code=f'ERR-SYS-{exc.status_code}-000',
        )
        return JSONResponse(status_code=api_exc.status, content=api_exc.to_dict())

    @app.exception_handler(APIException)
    async def unicorn_exception_handler(_: Request, api_exc: APIException):
        return JSONResponse(status_code=api_exc.status, content=api_exc.to_dict())

    @app.exception_handler(Exception)
    async def exception_handler(_: Request, exc: Exception):
        api_exc = APIException(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=str(exc),
            error_code='ERR-SYS-500-000',
        )
        return JSONResponse(status_code=api_exc.status, content=api_exc.to_dict())
