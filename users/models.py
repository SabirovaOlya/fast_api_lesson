from sqlalchemy import String, Float, Integer, UUID, ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.base import TimeModel
from datetime import date


class User(TimeModel):
    __tablename__ = 'users'

    fullname: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    position: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    birthday: Mapped[date] = mapped_column(DateTime, nullable=False)

    def __str__(self):
        return self.fullname
