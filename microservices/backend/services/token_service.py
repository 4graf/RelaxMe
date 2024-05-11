"""
Модуль для обработки JWT
"""

import datetime
import uuid
from typing import Tuple

import pytz
from fastapi import HTTPException
from jose import jwt, JWTError, ExpiredSignatureError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

settings = JwtSettings()


class JwtProcessorSingleton:
    """
    Класс для обработки JWT
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Вызывается при создании нового экземпляра.

            :param args: Не именнованые аргументы.
            :param kwargs: Именнованные аргументы.
        """

        session = kwargs.get("session")
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls)
            cls._instance.access_jwt_processor = AccessJwtProcessor(secret_key=settings.access_secret_key,
                                                                    session=session)
            cls._instance.refresh_jwt_processor = RefreshJwtProcessor(secret_key=settings.refresh_secret_key,
                                                                      session=session)

        return cls._instance


class JwtProcessor:
    """
    Базовый класс для обработки JWT
    """

    algorithm = 'HS256'

    def __init__(self, secret_key: str, session: AsyncSession):
        """
        Инициализирует экземпляр класса JwtProcessor.

            :param secret_key: Секретный ключ для создания и проверки подписи JWT.
            :param session: Сессия базы данных.
        """

        self.secret_key = secret_key
        self.session = session

    def _generate(self, delta_time_in_s: int, user_id: str, role: str) -> Tuple[str, str]:
        """
        Генерирует токен аутентификации.

            :param delta_time_in_s: Время действия токена в секундах.
            :param user_id: Идентификатор пользователя.
            :param role: Роль пользователя.
            :return:  Сгенерированный токен и его уникальный идентификатор.
        """

        request_tz = 'UTC'
        exp_time = datetime.datetime.now(pytz.timezone(request_tz)) + \
            datetime.timedelta(seconds=delta_time_in_s)
        token_id = str(uuid.uuid4())
        token = jwt.encode({
            'token_id': token_id,
            'role': role,
            'user_id': str(user_id),
            'exp': str(int(exp_time.timestamp()))
        }, self.secret_key, algorithm=self.algorithm)

        return token, token_id

    def _decode(self, token: str) -> UserRole:
        """
        Декодирование токена.

            :param token: Токен для декодирования.
            :return: Модель из словаря или None, если декодирование не удалось.
            :raise:
                TokenExpiredException, если токен истек.
                TokenCorruptedException, если токен поврежден.
        """

        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except ExpiredSignatureError as exc:
            raise TokenExpiredException from exc
        except JWTError as exc:
            raise TokenCorruptedException from exc
        return UserRole(**payload)


class AccessJwtProcessor(JwtProcessor):
    """
    Класс для работы с JWT доступа
    """

    def generate(self, user_id: str, role: str):
        """
        Создание токена доступа.

            :param user_id: Идентификатор пользователя.
            :param role: Роль пользователя.
            :return: Токен доступа.
        """

        return self._generate(settings.access_expiration, user_id, role)

    def decode(self, token: str) -> UserRole:
        """
        Декодирование токена доступа.

            :param token: Токен доступа.
            :return: Данные UserRole токена
        """

        return self._decode(token)

    async def refresh(self, token: str):
        """
        Обновление токена доступа.

            :param token: Токен доступа.
            :return: Новый токен доступа.
            :raise: HTTPException: Если токен недействителен или пользователь не найден.
        """

        payload = self.decode(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user_id = payload['user_id']

        try:
            user_repo = UsersRepository(session=self.session)
            await user_repo.get_user(user_id=user_id)
        except NoResultFound as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Пользователь не найден",
                headers={"WWW-Authenticate": "Bearer"},
            ) from exc

        return self.generate(user_id)


class RefreshJwtProcessor(JwtProcessor):
    """
    Класс для работы с JWT обновления
    """

    def generate(self, user_id: str, role: str):
        """
        Создание токена обновления.

            :param user_id: Идентификатор пользователя.
            :param role: Роль пользователя.
            :return: Токен обновления.
        """

        return self._generate(settings.refresh_expiration, user_id, role)

    def decode(self, token: str):
        """
        Декодирование токена обновления.

            :param token: Токен.
            :return: Полезная нагрузка (payload) токена или None, если токен невалиден.
        """

        return self._decode(token)
