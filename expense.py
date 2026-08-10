from enum import Enum, auto
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List
import itertools

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
    """Class that stores information about singular expense"""
    amount: float
    category: ExpenseCategory = ExpenseCategory.Others
    date: datetime = datetime.now()

class ExpenseManager:

    expenses: Dict[int, Expense]

    _id_iter = itertools.count()

    def __init__(self, expenses: List[Expense] = list()):
        self.expenses = dict()
        for expense in expenses:
            next_id = next(self._id_iter)
            self.expenses[next_id] = expense
    
   
    def _validate_expense(self, expense: Expense):
        conditions = [
                expense.amount >= 0
                ]
        return all(conditions)

    def _print_expenses(self):
        for id, expense in self.expenses.items():
            print(f"Id: {id}, Expense:{expense}")


    def add(self, expense: Expense):
        if self._validate_expense(expense):
            next_id = next(self._id_iter)
            self.expenses[next_id] = expense
        else:
            print("Error! Invalid expense")

    def find_by_id(self, target_id: int) -> Expense | None:
        target_expense = self.expenses.get(target_id)
        if target_expense is None:
            print("Expense with such id is nowhere to be found")
            return None
        return target_expense

    def delete(self, target_id: int) -> bool:
        if self.expenses.get(target_id) is None:
            return False
        self.expenses.pop(target_id)
        return True
