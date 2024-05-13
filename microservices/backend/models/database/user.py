from uuid import UUID

from sqlalchemy import text, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'user_app'
    # __tablename__ = 'user_account'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    login: Mapped[str] = mapped_column(String(length=64), unique=True)
    password_hash: Mapped[str] = mapped_column(String(length=1024), unique=True)
    safe_place_id: Mapped[UUID] = mapped_column(ForeignKey("safe_place.id"), nullable=True)

    safe_place: Mapped["SafePlaceModel"] = relationship(back_populates='users')
