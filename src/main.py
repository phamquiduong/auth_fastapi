from fastapi.middleware.cors import CORSMiddleware

from exceptions.handler import handler_exception
from fastapi import FastAPI
from routers import auth_router, user_router
from settings import settings

app = FastAPI(
    title="FastAPI Authentication",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler
handler_exception(app)

# Include routers
app.include_router(auth_router)
app.include_router(user_router)
