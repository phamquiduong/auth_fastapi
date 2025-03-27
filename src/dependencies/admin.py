from typing import Annotated

from fastapi import Depends

from constants.role import Role
from dependencies.user import CurrentUserDependency
from exceptions.auth import NotPremissionException
from models.user import Users


async def get_admin_user(user: CurrentUserDependency):
    if user.role != Role.ADMIN:
        raise NotPremissionException

    return user


AdminUserDependency = Annotated[Users, Depends(get_admin_user)]
