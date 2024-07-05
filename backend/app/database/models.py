from sqlalchemy import (
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship, mapped_column, relationship, Mapped
from typing import List
from .connection import Base


class Company(Base):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(100))
    address: Mapped[str] = mapped_column(String(300))
    timezone: Mapped[str] = mapped_column(String(100))
    user: Mapped[List["User"]] = relationship(back_populates="company")


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    identification: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(300))
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id"))
