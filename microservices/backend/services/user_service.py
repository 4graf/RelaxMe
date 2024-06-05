import uuid
from uuid import UUID

from microservices.backend.exceptions.user_esceptions import UserNotFoundException
from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.interfaces.services.abstract_user_service import AbstractUserService
from microservices.backend.repositories.database.user_repository import UserRepository
from microservices.backend.schemas.user import User, UserLogin


class UserService(AbstractUserService):
    user_repo: AbstractUserRepository

    def __init__(self, user_repo: AbstractUserRepository):
        """
        Инициализация сервиса для работы с пользователями.

            :param user_repo: Репозиторий для работы с пользователями.
        """

        self.user_repo = user_repo

    async def login_user(self, user_login: UserLogin) -> User:
        try:
            exist_user = await self.user_repo.get_user_by_login(user_login.login)
            return exist_user
        except UserNotFoundException:
            user = User(id=uuid.uuid4(),
                        login=user_login.login,
                        password_hash=user_login.password)  # ToDo: хэшировать
                        # safe_place_id=None)
            await self.user_repo.add_user(user)
            return user

    async def get_user(self, id_: UUID) -> User:
        user = await self.user_repo.get_user(id_)
        return user

    async def get_user_by_login(self, login: str) -> User:
        user = await self.user_repo.get_user_by_login(login)
        return user

    async def get_all_users(self) -> list[User]:
        users = await self.user_repo.get_all_users()
        return users
