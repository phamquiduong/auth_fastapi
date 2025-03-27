from fastapi import status

from exceptions import APIException

UserAlreadyExistsException = APIException(
    status=status.HTTP_409_CONFLICT,
    message='User already exists',
    error_code='ERR-USER-409-001',
    error_fields={
        'email': 'Email already exists',
    }
)

UserDoestNotExistException = APIException(
    status=status.HTTP_404_NOT_FOUND,
    message='User does not exists',
    error_code='ERR-USER-404-001',
    error_fields={
        'email': 'Email doest not exists',
    }
)
