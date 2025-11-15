Python code (≈65 lines) 👇

import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Function to add new expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount: ₹"))
    note = input("Enter note (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            print("\nDate\t\tCategory\tAmount\tNote")
            print("-" * 50)
            total = 0
            for row in reader:
                if len(row) == 4:
                    print(f"{row[0]}\t{row[1]}\t₹{row[2]}\t{row[3]}")
                    total += float(row[2])
            print("-" * 50)
            print(f"Total Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("⚠ No expense records found!\n")

# Function to view expenses by category
def view_by_category():
    category = input("Enter category to view: ")
    try:
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            total = 0
            print(f"\nExpenses in '{category}' category:")
            print("-" * 40)
            for row in reader:
                if len(row) == 4 and row[1].lower() == category.lower():
                    print(f"{row[0]} - ₹{row[2]} ({row[3]})")
                    total += float(row[2])
            print("-" * 40)
            print(f"Total in this category: ₹{total}\n")
    except FileNotFoundError:
        print("⚠ No data found!\n")

# Main menu
def main():
    print("\n💸 Welcome to Expense Tracker 💸\n")

    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            print("👋 Thank you for using Expense Tracker!")
            break
        else:
            print("❌ Invalid choice! Please try again.\n")

if _name_ == "_main_":
    main()
