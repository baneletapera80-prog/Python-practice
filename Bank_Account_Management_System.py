bank_accounts = []

def create_account(account_number, account_holder, initial_balance):
    account = {
        'account_number': account_number,
        'account_holder': account_holder,
        'balance': initial_balance
    }
    bank_accounts.append(account)
    return account
def view_accounts():

    if not bank_accounts:
        print("No bank accounts found.")
        return
    print("\nBank Account List:")
    for index, account in enumerate(bank_accounts, start=1):
        print(f"{index}. Account Number: {account['account_number']}, Holder: {account['account_holder']}, Balance: ${account['balance']:.2f}")

def search_account(account_number):
    for account in bank_accounts:
        if account['account_number'] == account_number:
            return account
    return None

def deposit(account_number, amount):
    account = search_account(account_number)
    if account:
        account['balance'] += amount
        return True
    return False

def withdraw(account_number, amount):
    account = search_account(account_number)
    if account:
        if account['balance'] >= amount:
            account['balance'] -= amount
            return True
        else:
            print("Insufficient balance.")
            return False
    return False

def transfer(from_account_number, to_account_number, amount):
    from_account = search_account(from_account_number)
    to_account = search_account(to_account_number)
    if from_account and to_account:
        if from_account['balance'] >= amount:
            from_account['balance'] -= amount
            to_account['balance'] += amount
            return True
        else:
            print("Insufficient balance in the source account.")
            return False
    return False

def delete_account(account_number):
    account = search_account(account_number)
    if account:
        bank_accounts.remove(account)
        return True
    return False

def save_accounts_to_file(filename):
    with open(filename, 'w') as file:
        for account in bank_accounts:
            file.write(f"{account['account_number']},{account['account_holder']},{account['balance']}\n")

def load_accounts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                account_number, account_holder, balance = line.strip().split(',')
                create_account(account_number, account_holder, float(balance))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty account list.")

def main():
    load_accounts_from_file('accounts.txt')
    while True:
        print("\nBank Account Management System")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Search Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Delete Account")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            create_account(account_number, account_holder, initial_balance)
            print("Account created successfully.")
        elif choice == '2':
            view_accounts()
        elif choice == '3':
            account_number = input("Enter account number to search: ")
            account = search_account(account_number)
            if account:
                print(f"Account Number: {account['account_number']}, Holder: {account['account_holder']}, Balance: ${account['balance']:.2f}")
            else:
                print("Account not found.")
        elif choice == '4':
            account_number = input("Enter account number to deposit into: ")
            amount = float(input("Enter amount to deposit: "))
            if deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Account not found.")
        elif choice == '5':
            account_number = input("Enter account number to withdraw from: ")
            amount = float(input("Enter amount to withdraw: "))
            if withdraw(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed.")
        elif choice == '6':
            from_account_number = input("Enter source account number: ")
            to_account_number = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            if transfer(from_account_number, to_account_number, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")
        elif choice == '7':
            account_number = input("Enter account number to delete: ")
            if delete_account(account_number):
                print("Account deleted successfully.")
            else:
                print("Account not found.")
        elif choice == '8':
            save_accounts_to_file('accounts.txt')
            print("Exiting the system. Goodbye!")
            break

if __name__ == "__main__":
    main()