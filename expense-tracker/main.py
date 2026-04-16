from database import connect, add_expense, view_expenses, delete_expense, monthly_summary
from analysis import plot_monthly_expenses

def menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    print("5. Monthly Summary")
    print("6. Show Expense Chart")

def main():
    connect()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter title: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")

            add_expense(title, amount, category, date)
            print("✅ Expense Added!")

        elif choice == '2':
            expenses = view_expenses()
            print("\n--- Expenses ---")
            for exp in expenses:
                print(exp)

        elif choice == '3':
            exp_id = int(input("Enter Expense ID to delete: "))
            delete_expense(exp_id)
            print("❌ Expense Deleted!")

        elif choice == '4':
            print("Exiting...")
            break

        elif choice == '5':
            summary = monthly_summary()
            print("\n--- Monthly Summary ---")
            for month, total in summary:
                print(f"{month} : {total}")

        elif choice == '6':
            plot_monthly_expenses()

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
