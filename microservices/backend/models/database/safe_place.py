from uuid import UUID

from sqlalchemy import text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import Base


class SafePlace(Base):
    __tablename__ = 'safe_place'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    ...

    users: Mapped[list["User"]] = relationship(back_populates='safe_place')
