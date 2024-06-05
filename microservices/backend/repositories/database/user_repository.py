import logging
from uuid import UUID

from sqlalchemy import select

from microservices.backend.exceptions.user_esceptions import UserNotFoundException
from microservices.backend.interfaces.repositories.abstract_user_repository import AbstractUserRepository
from microservices.backend.models.database.user import UserModel
from microservices.backend.repositories.database.base import BaseDBRepository
from microservices.backend.schemas.user import User


class UserRepository(AbstractUserRepository, BaseDBRepository):
    model = UserModel

    async def add_user(self, user: User) -> User:
        user = await self._add(user.model_dump())
        return User.model_validate(user)

    async def get_user(self, id_: UUID) -> User:
        user = await self._get(id_)
        if not user:
            raise UserNotFoundException
        return User.model_validate(user)

    async def get_user_by_login(self, login: str) -> User:
        stmt = select(self.model).filter(self.model.login == login)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()
        if not user:
            raise UserNotFoundException

        return User.model_validate(user)

    async def get_all_users(self) -> list[User]:
        users = await self._get_all()
        return [User.model_validate(user) for user in users]
