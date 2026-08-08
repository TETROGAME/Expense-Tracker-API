from enum import Enum, auto
from datetime import datetime
from dataclasses import dataclass
from typing import List

class ExpenseCategory(Enum):
    Groceries = auto()
    Leisure = auto()
    Electronics = auto()
    Utilities = auto()
    Clothing = auto()
    Health = auto()
    Others = auto()

@dataclass
class Expense:
    amount: float
    category: ExpenseCategory = ExpenseCategory.Others
    date: datetime = datetime.now()

class ExpenseManager:
    expenses: List[Expense]
    def __init__(self, expenses: List[Expense] = list()):
        self.expenses = expenses
    
   
    def _validate_expense(self, expense: Expense):
        conditions = [
                expense.amount >= 0
                ]
        return all(conditions)


    def add_expense(self, expense: Expense):
        if self._validate_expense(expense):
            self.expenses.append(expense)
        else:
            print("Error! Invalid expense")
