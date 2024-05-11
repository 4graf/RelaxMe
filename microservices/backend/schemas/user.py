from uuid import UUID

from microservices.backend.schemas.base import BaseSchema


class User(BaseSchema):
    id: UUID
    login: str
    password_hash: str
    safe_place: list[SafePlace]
