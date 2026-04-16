import matplotlib.pyplot as plt
from database import monthly_summary

def plot_monthly_expenses():
    data = monthly_summary()

    if not data:
        print("No data to display")
        return

    months = [row[0] for row in data]
    totals = [row[1] for row in data]

    plt.figure()
    plt.bar(months, totals)
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.title("Monthly Expense Summary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
