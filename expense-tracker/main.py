from database import connect, add_expense, view_expenses, delete_expense

def menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

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

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
