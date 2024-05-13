from datetime import datetime
from uuid import UUID

from numpy import ndarray
from sqlalchemy import text, String, ForeignKey, DateTime, func, ARRAY, Double, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import BaseModel


class EEGModel(BaseModel):
    __tablename__ = 'eeg'

    # id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    added_at: Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user_app.id"), primary_key=True)
    state: Mapped[int] = mapped_column(SmallInteger())
    values: Mapped[list[float]] = mapped_column(ARRAY(Double, dimensions=2))

    # user: Mapped["UserModel"] = relationship(back_populates='eeg')
