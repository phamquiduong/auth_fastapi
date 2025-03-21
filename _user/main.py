from fastapi import FastAPI

from routers.user import router as user_router

app = FastAPI(
    title="User API",
    openapi_url='/users/openapi.json',
    docs_url='/users/docs',
    redoc_url='/users/redoc',
)
app.include_router(user_router)
