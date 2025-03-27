from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from settings.database import ENGINE


def get_session():
    with Session(ENGINE) as session:
        yield session
        session.commit()


SessionDependency = Annotated[Session, Depends(get_session)]
