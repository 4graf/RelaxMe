"""Классы исключений для пользователей"""


class UserException(Exception):
    """Базовое исключение для пользователей"""


class UserNotFoundException(UserException):
    """Исключение, при не нахождении пользователя"""

    def __init__(self, msg='User not found.'):
        super().__init__(msg)
