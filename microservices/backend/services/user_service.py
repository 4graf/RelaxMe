from uuid import UUID

from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.interfaces.services.abstract_user_service import AbstractUserService
from microservices.backend.repositories.database.user_repository import UserRepository
from microservices.backend.schemas.user import User


class UserService(AbstractUserService):
    user_repo: AbstractUserRepository

    def __init__(self, user_repo: UserRepository):
        """
        Инициализация сервиса для работы с пользователями.

            :param user_repo: Репозиторий для работы с пользователями.
        """

        self.user_repo = user_repo

    async def add_user(self, user: User) -> None:
        await self.user_repo.add_user(user)

    async def get_user(self, id_: UUID) -> User:
        user = await self.user_repo.get_user(id_)
        return user
