from tracker.db import init_db
from tracker.tracker import add_expense, get_expenses, get_total_spent

def main():
    init_db()

    while True:
        print("\nExpense Tracker CLI")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(amount, category, date)
            print("Expense added.")

        elif choice == "2":
            for exp in get_expenses():
                print(exp)

        elif choice == "3":
            print(f"Total spent: ₹{get_total_spent():.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()