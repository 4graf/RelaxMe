from abc import ABC
from typing import Any, Sequence
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from microservices.backend.models.database.base import BaseModel

Payload = dict[str, Any]


class BaseDBRepository(ABC):
    model: type[BaseModel]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _add(self, data: Payload | list[Payload]) -> BaseModel | Sequence[BaseModel]:
        stmt = (
            self.model.insert()
            .values(data)
            .returning(self.model)
        )

        result = await self.session.execute(stmt)
        result = result.scalars().all()
        await self.session.commit()
        return result[0] if len(result) == 1 else result

    async def _update(self, id_: UUID, data: Payload) -> BaseModel:
        stmt = (
            self.model.update()
            .values(data)
            .filter(self.model.id == id_)
            .returning(self.model)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one()
        await self.session.commit()
        return result

    async def _get(self, id_: UUID) -> BaseModel:
        stmt = (
            self.model.select()
            .filter(self.model.id == id_)
        )

        result = await self.session.execute(stmt)
        result = result.scalar_one_or_none()
        await self.session.commit()
        return result

    async def _get_all(self) -> Sequence[BaseModel]:
        stmt = (
            self.model.select()
        )

        result = await self.session.execute(stmt)
        result = result.scalars().all()
        await self.session.commit()
        return result
