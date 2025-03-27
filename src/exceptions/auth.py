from fastapi import status

from exceptions.base import APIException

# 400
PasswordIncorrectException = APIException(
    status=status.HTTP_400_BAD_REQUEST,
    message='Incorrect password',
    error_code='ERR-AUTH-400-001',
    error_fields={
        'password': 'Incorrect password',
    }
)

# 401
TokenInvalidException = APIException(
    status=status.HTTP_401_UNAUTHORIZED,
    message='Could not validate credentials',
    error_code='ERR-AUTH-401-001',
    error_fields={
        'WWW-Authenticate': 'Token Invalid',
    }
)

TokenExpiredException = APIException(
    status=status.HTTP_401_UNAUTHORIZED,
    message='Could not validate credentials',
    error_code='ERR-AUTH-401-002',
    error_fields={
        'WWW-Authenticate': 'Token Expired',
    }
)

TokenTypeIncorrectException = APIException(
    status=status.HTTP_401_UNAUTHORIZED,
    message='Could not validate credentials',
    error_code='ERR-AUTH-401-003',
    error_fields={
        'WWW-Authenticate': 'Token type incorrect',
    }
)

# 403
NotPremissionException = APIException(
    status=status.HTTP_403_FORBIDDEN,
    message='User not permission',
    error_code='ERR-AUTH-403-001',
    error_fields={
        'WWW-Authenticate': 'User not permission',
    }
)
