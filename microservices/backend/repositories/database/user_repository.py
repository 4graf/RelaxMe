import logging
from uuid import UUID

from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.models.database.user import UserModel
from microservices.backend.repositories.database.base import BaseDBRepository
from microservices.backend.schemas.user import User


class UserRepository(AbstractUserRepository, BaseDBRepository):
    model = UserModel

    async def add_user(self, user: User) -> None:
        await self._add(user.model_dump())

    async def get_user(self, id_: UUID) -> User:
        user = await self._get(id_)
        return User.model_validate(user)

    async def get_all_users(self) -> list[User]:
        users = await self._get_all()
        logging.warning(users)
        return [User.model_validate(user) for user in users]
