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
