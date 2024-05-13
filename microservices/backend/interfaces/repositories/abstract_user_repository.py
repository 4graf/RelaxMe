from abc import ABC, abstractmethod
from uuid import UUID

from microservices.backend.schemas.eeg import EEGData
from microservices.backend.schemas.user import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def add_user(self, user: User) -> None:
        ...

    @abstractmethod
    async def get_user(self, id_: UUID) -> User:
        ...

    @abstractmethod
    async def get_all_users(self) -> list[User]:
        ...
