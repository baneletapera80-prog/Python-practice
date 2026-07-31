expense = []

def add_expense(amount, category):
    expense.append({'amount': amount, 'category': category})

def get_total_expenses():
    return sum(item['amount'] for item in expense)

def get_expenses_by_category(category):
    return [item for item in expense if item['category'] == category]

def clear_expenses():
    expense.clear() 

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Clear All Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_expense(amount, category)
            print(f"Added expense: {amount} in category '{category}'.")

        elif choice == '2':
            total = get_total_expenses()
            print(f"Total expenses: R{total:.2f}")

        elif choice == '3':
            category = input("Enter category to view expenses: ")
            expenses_in_category = get_expenses_by_category(category)
            if expenses_in_category:
                print(f"Expenses in category '{category}':")
                for item in expenses_in_category:
                    print(f"- Amount: {item['amount']}")
            else:
                print(f"No expenses found in category '{category}'.")

        elif choice == '4':
            clear_expenses()
            print("All expenses cleared.")

        elif choice == '5':
            print("Exiting Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
