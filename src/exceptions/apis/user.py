from fastapi import status

from exceptions.base import APIException

# 404
UserDoestNotExistException = APIException(
    status=status.HTTP_404_NOT_FOUND,
    message='User does not exists',
    error_code='ERR-USER-404-001',
    error_fields={
        'user_id': 'User id is not exists',
    }
)

EmailDoestNotExistException = APIException(
    status=status.HTTP_404_NOT_FOUND,
    message='User does not exists',
    error_code='ERR-USER-404-002',
    error_fields={
        'email': 'Email is not exists',
    }
)

# 409
UserAlreadyExistsException = APIException(
    status=status.HTTP_409_CONFLICT,
    message='User already exists',
    error_code='ERR-USER-409-001',
    error_fields={
        'email': 'Email already exists',
    }
)
