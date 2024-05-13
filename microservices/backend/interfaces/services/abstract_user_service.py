from abc import ABC, abstractmethod
from uuid import UUID

from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.schemas.user import User, UserLogin


class AbstractUserService(ABC):
    user_repo: AbstractUserRepository

    @abstractmethod
    async def login_user(self, user: UserLogin) -> User:
        ...

    @abstractmethod
    async def get_user(self, id_: UUID) -> User:
        ...

    @abstractmethod
    async def get_user_by_login(self, login: str) -> User:
        ...

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        ...
