# Buiilding a simple expenses tracker .

expenses = []

# This is where a user can add all his expenses ( amount, catagroy, description)
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    
    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    
    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses found.\n")
        return
    
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']} | {expense['category']} | {expense['description']}")
    print()


def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total Spending: ₹{total}\n")



def menu():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice\n")


menu()
