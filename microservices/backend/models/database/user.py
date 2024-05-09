from uuid import UUID

from sqlalchemy import text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    login: Mapped[str] = mapped_column(String(length=64), unique=True)
    password_hash: Mapped[str] = mapped_column(String(length=1024), unique=True)

    safe_place: Mapped["SafePlace"] = relationship(back_populates='users')
