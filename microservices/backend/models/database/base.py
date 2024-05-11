"""
Модуль Base

Этот модуль предоставляет базовую модель для SQLAlchemy моделей.

"""
from sqlalchemy.orm import declarative_base

DeclarativeBase = declarative_base()


class BaseModel(DeclarativeBase):
    """
    Базовая модель для SQLAlchemy моделей.
    """

    __abstract__ = True
