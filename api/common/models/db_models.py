from typing import Optional
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text


class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Categorie(db.Model):
    __tablename__ = 'categories'
    category_id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    category_name: Mapped[str] = mapped_column(String(15))
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    picture: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)

class Customer(db.Model):
    __tablename__ = 'customers'
    customer_id: Mapped[str] = mapped_column(String(5), primary_key=True)
    company_name: Mapped[str] = mapped_column(String(40))
    contact_name: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    contact_title: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    region: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    postal_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(15), nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(24), nullable=True)
    fax: Mapped[Optional[str]] = mapped_column(String(24), nullable=True)
    login: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    password_hash: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    role_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
