import sqlite3
import csv

def export_to_csv():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()

    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Title", "Amount", "Category", "Date"])
        writer.writerows(data)

    print("✅ Data exported to expenses.csv")
