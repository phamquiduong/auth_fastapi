from fastapi import status

from exceptions import APIException

PasswordIncorrectException = APIException(
    status=status.HTTP_400_BAD_REQUEST,
    message='Incorrect password',
    error_code='ERR-AUTH-400-001',
    error_fields={
        'password': 'Incorrect password',
    }
)
