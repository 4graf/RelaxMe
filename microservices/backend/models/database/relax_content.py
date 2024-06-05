from uuid import UUID

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from microservices.backend.models.database.base import BaseModel


class RelaxContentModel(BaseModel):
    __tablename__ = 'relax_content'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('gen_random_uuid()'))
    content_url: Mapped[str] = mapped_column(unique=True)
    safe_place_id: Mapped[UUID] = mapped_column(ForeignKey("safe_place.id"))

    safe_place: Mapped["SafePlaceModel"] = relationship(back_populates='relax_contents')
