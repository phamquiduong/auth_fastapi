from sqlmodel import create_engine

from settings import settings

CONNECT_ARGS = {"check_same_thread": False}
ENGINE = create_engine(settings.DATABASE_URL, connect_args=CONNECT_ARGS)
