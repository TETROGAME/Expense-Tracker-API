from expense_tracker_api.expense import Expense, ExpenseManager


def main():
    expense1 = Expense(amount=99)
    expense2 = Expense(amount=-1)
    expense3 = Expense(amount=67)
    expense4 = Expense(amount=4)
    mgr = ExpenseManager()
    mgr.add(expense1)
    mgr.add(expense2)
    mgr.add(expense3)
    mgr.add(expense4)

    mgr._print_expenses()

    mgr.delete(0)
    mgr.delete(-1)
    print("\n")

    mgr._print_expenses()

    expense5 = Expense(amount=12355)
    mgr.add(expense5)

    mgr._print_expenses()


if __name__ == "__main__":
    main()
