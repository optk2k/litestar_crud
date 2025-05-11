import datetime

from advanced_alchemy.base import BigIntAuditBase
from msgspec import Struct
from sqlalchemy.orm import Mapped


class UserModel(BigIntAuditBase):
    __tablename__ = "user"

    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]


class UserGetSchema(Struct):
    id: int
    name: str
    surname: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserUpdateSchema(Struct):
    name: str
    surname: str
    password: str


class UserCreateSchema(Struct):
    name: str
    surname: str
    password: str
