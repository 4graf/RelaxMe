from abc import ABC, abstractmethod

from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.schemas.user import User


class AbstractUserService(ABC):
    user_repo: AbstractUserRepository

    @abstractmethod
    async def add_user(self, user: User) -> None:
        ...

    @abstractmethod
    async def get_user(self, user: User) -> User:
        ...
