from uuid import UUID

from microservices.backend.schemas.base import BaseSchema
from microservices.backend.schemas.safe_place import SafePlace


class User(BaseSchema):
    id: UUID
    login: str
    password_hash: str
    safe_place_id: UUID | None = None


class UserAdd(BaseSchema):
    login: str
    password: str


class UserResponse(BaseSchema):
    login: str
    password: str
    safe_place: list[SafePlace] | None = None

