from typing import Annotated

from fastapi import Depends

from constants import Role
from dependencies.user import CurrentUserDependency
from exceptions import NotPremissionException
from models import Users


async def get_admin_user(user: CurrentUserDependency):
    if user.role != Role.ADMIN:
        raise NotPremissionException

    return user


AdminUserDependency = Annotated[Users, Depends(get_admin_user)]
