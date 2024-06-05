from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import BaseModel


class SafePlaceModel(BaseModel):
    __tablename__ = 'safe_place'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    keys: Mapped[str] = mapped_column(unique=True)

    users: Mapped[list["UserModel"]] = relationship(back_populates='safe_place')
    relax_contents: Mapped[list["RelaxContentModel"]] = relationship(back_populates='safe_place')
