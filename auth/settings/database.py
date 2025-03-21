from sqlmodel import create_engine

from settings import settings

connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url, connect_args=connect_args)
