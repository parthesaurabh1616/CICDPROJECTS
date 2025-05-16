from tracker.tracker import add_expense, get_expenses, get_total_spent
from tracker.db import init_db
import os

def test_add_and_total_expense():
    init_db()
    add_expense(500, "Food", "2025-05-15")
    add_expense(200, "Travel", "2025-05-15")
    expenses = get_expenses()
    assert len(expenses) >= 2
    assert get_total_spent() >= 700