from datetime import datetime, timedelta, timezone
from enum import Enum, auto

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class ExpenseCategory(Enum):
    Groceries = auto()
    Leisure = auto()
    Electronics = auto()
    Utilities = auto()
    Clothing = auto()
    Health = auto()
    Others = auto()


class ExpenseORM(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float]
    category: Mapped[ExpenseCategory]
    description: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(tz=timezone(timedelta(hours=3)))
    )
