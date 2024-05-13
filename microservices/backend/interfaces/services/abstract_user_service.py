from abc import ABC, abstractmethod
from uuid import UUID

from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.schemas.user import User, UserAdd


class AbstractUserService(ABC):
    user_repo: AbstractUserRepository

    @abstractmethod
    async def add_user(self, user: UserAdd) -> None:
        ...

    @abstractmethod
    async def get_user(self, id_: UUID) -> User:
        ...

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        ...
