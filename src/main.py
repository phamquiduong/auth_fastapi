from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import APIException
from routers.auth import auth_router
from routers.user import user_router

app = FastAPI(
    title="User API",
    openapi_url='/users/openapi.json',
    docs_url='/users/docs',
    redoc_url='/users/redoc',
)


# Exception handler
@app.exception_handler(APIException)
async def unicorn_exception_handler(request: Request, api_exc: APIException):
    return JSONResponse(
        status_code=api_exc.status,
        content=api_exc.to_dict(),
    )


# Include routers
app.include_router(user_router)
app.include_router(auth_router)
