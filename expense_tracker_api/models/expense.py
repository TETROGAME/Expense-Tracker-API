from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Expense(Base):
    __tablename__ = "expenses"
