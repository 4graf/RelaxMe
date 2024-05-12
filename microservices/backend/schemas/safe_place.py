from uuid import UUID

from microservices.backend.schemas.base import BaseSchema


class SafePlace(BaseSchema):
    id: UUID
    ...
