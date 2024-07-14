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
    phone: Mapped[str] = mapped_column(String(300))
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("company.id"))
    company: Mapped["Company"] = relationship("Company", back_populates="user")


class Media(Base):
    __tablename__ = "media"
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(100))


class CompanyMedia(Base):
    __tablename__ = "companymedia"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("company.id"))
    company: Mapped["Company"] = relationship("Company", back_populates="companymedia")
    media_id: Mapped[int] = mapped_column(Integer, ForeignKey("media.id"))
    media: Mapped["Media"] = relationship("Media", back_populates="companymedia")
