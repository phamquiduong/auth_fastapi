from fastapi import FastAPI

from exceptions.handler import handler_exception
from routers import auth_router, user_router

app = FastAPI(
    title="FastAPI Authentication",
)

# Exception handler
handler_exception(app)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
