"""
Модуль Base

Этот модуль предоставляет базовую модель для SQLAlchemy моделей.

"""
from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    """
    Базовая модель для SQLAlchemy моделей.
    """

    __abstract__ = True
