from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions.base import APIException
from routers import auth_router, user_router

app = FastAPI(
    title="FastAPI Authentication",
)


# Exception handler
@app.exception_handler(APIException)
async def unicorn_exception_handler(_: Request, api_exc: APIException):
    return JSONResponse(
        status_code=api_exc.status,
        content=api_exc.to_dict(),
    )


# Include routers
app.include_router(auth_router)
app.include_router(user_router)
