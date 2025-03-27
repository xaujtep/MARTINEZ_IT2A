<<<<<<< HEAD
#BANK SIMULATION PROGRAM 
#Create new account
#if account exist, deposit, withdraw, checkbalance -- function 
#if deposit, enter amount, give filipino denomation breakdown 
#if wihdraw, you cannot withdraw if balance is lower than withdraw amount 
#deposit, ask how much? and show current balance 
#continue to repeat the process until user opt out or exit the program, use while loop 
#you will create a function that will breakdown a filipino denomination and then print it 
#Create a python proram

accounts = {
    1002: {"name": "Stephanie"},
    2002: {"name": "June"},
    3002: {"name": "Xauj"},
}

def check_account(account_number):
    
    if account_number in accounts:
        print(f"Account {account_number} exists!")
        print(f"Account Holder: {accounts[account_number]['name']}")
    else:
        print(f"Account {account_number} does not exist.\n")

# Main Program
while True:
    print("Bank Account Checker")
    print("1. Check an account")
    print("2. Exit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        account_number = int(input("Enter the account number to check: "))
        check_account(account_number)
        print("Please enter a valid number.\n")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 or 2.\n")


    def show_balance(balance):
        print(f"Your balance is ₱{balance:.2f}")

    def deposit():
        amount = float(input("Enter an amount to be deposited: "))

        if amount < 0:
            print("Invalid Amount")
            return 0
        else:
            return amount
    def withdraw(balance):
        amount = float(input("Enter amount to be withdrawn: "))

        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must larger than 0")
            return 0
        else:
            return amount

    def main():
        balance = 0
        is_running = True

        while is_running:
            print("Bank Program")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1" :
                show_balance(balance)
            elif choice == "2":
                balance += deposit()
            elif choice == "3":
                balance -= withdraw(balance)
            elif choice == "4":
                is_running = False
            else:
                print("That is not a valid choice")
        print("Thank you, have a nice day!")
    if __name__ == "__main__":
        main()
=======
#BANK SIMULATION PROGRAM 
#Create new account
#if account exist, deposit, withdraw, checkbalance -- function 
#if deposit, enter amount, give filipino denomation breakdown 
#if wihdraw, you cannot withdraw if balance is lower than withdraw amount 
#deposit, ask how much? and show current balance 
#continue to repeat the process until user opt out or exit the program, use while loop 
#you will create a function that will breakdown a filipino denomination and then print it 
#Create a python proram

accounts = {
    1002: {"name": "Stephanie"},
    2002: {"name": "June"},
    3002: {"name": "Xauj"},
}

def check_account(account_number):
    
    if account_number in accounts:
        print(f"Account {account_number} exists!")
        print(f"Account Holder: {accounts[account_number]['name']}")
    else:
        print(f"Account {account_number} does not exist.\n")

# Main Program
while True:
    print("Bank Account Checker")
    print("1. Check an account")
    print("2. Exit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        account_number = int(input("Enter the account number to check: "))
        check_account(account_number)
        print("Please enter a valid number.\n")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 or 2.\n")


    def show_balance(balance):
        print(f"Your balance is ₱{balance:.2f}")

    def deposit():
        amount = float(input("Enter an amount to be deposited: "))

        if amount < 0:
            print("Invalid Amount")
            return 0
        else:
            return amount
    def withdraw(balance):
        amount = float(input("Enter amount to be withdrawn: "))

        if amount > balance:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must larger than 0")
            return 0
        else:
            return amount

    def main():
        balance = 0
        is_running = True

        while is_running:
            print("Bank Program")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1" :
                show_balance(balance)
            elif choice == "2":
                balance += deposit()
            elif choice == "3":
                balance -= withdraw(balance)
            elif choice == "4":
                is_running = False
            else:
                print("That is not a valid choice")
        print("Thank you, have a nice day!")
    if __name__ == "__main__":
        main()
>>>>>>> afb4775 (Initial commit)
