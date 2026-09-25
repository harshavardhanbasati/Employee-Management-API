from sqlalchemy import Column, Float, Integer, String

from .database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    department = Column(
        String,
        nullable=False
    )

    salary = Column(
        Float,
        nullable=False
    )