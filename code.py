import csv
import os


def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")


    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")

def view_expenses():

    if not os.path.exists("expenses.csv"):
        print("No expenses recorded yet.\n")
        return

    print("\nExpense Records:")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:

            print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")
    print("\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
