<<<<<<< HEAD

balance = 0

def create_account(name, initial_deposit = 0):
    account_name = name
    global balance
    balance = initial_deposit
    print(f"Account created for \n{account_name} with initial deposit of {balance} pesos")

def deposit(amoount):
    global balance
    balance += amount
    print(f"Amount deposited {amount}")
    check_balance

def check_balance():
    global balance
    print(f"Current balance is {balance}")

def withdraw(amount):
    global balance
    balance -= amount
    print(f"AMOUNT WITHDRAW {amount}") 
    check_balance()

def denomination():
    libo = amount // 1000
    libo_sukli = amount % 1000

    five_h = libo_sukli // 500
    five_sukli = amount % 500

    two_h = five_sukli // 200
    two_sukli = amount % 200

    one_h = two_sukli // 100
    one_sukli = amount %  100

    five_t = one_sukli // 50
    five_sukli = amount % 50

jvp = True
while jvp == True:
    print("WELCOME TO MY BANK SIMULATOR PROGRAM")
    print("======================================")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Balance")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("CREATE ACCOUNT")
        print("PLEASE PROVIDE THE FOLLOWING INFORMATION")
        fullname = input("Enter your name: ")
        print("MUST PROVIDE INITIAL DEPOSIT")
        amount = eval(input("Enter your amount for your initial deposit: "))
        create_account(fullname, amount)

    elif choice == "2":
        print("============== DEPOSIT =============")
        amount = eval(input("Enter your amount: "))
        deposit(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("============ WITHDRAW =============")
        amount = eval(input("Enter the amount: "))
        withdraw(amount)

    elif choice == "5":
        print("Thank you for stopping by")

    else:
        break
    
=======

balance = 0

def create_account(name, initial_deposit = 0):
    account_name = name
    global balance
    balance = initial_deposit
    print(f"Account created for \n{account_name} with initial deposit of {balance} pesos")

def deposit(amoount):
    global balance
    balance += amount
    print(f"Amount deposited {amount}")
    check_balance

def check_balance():
    global balance
    print(f"Current balance is {balance}")

def withdraw(amount):
    global balance
    balance -= amount
    print(f"AMOUNT WITHDRAW {amount}") 
    check_balance()

def denomination():
    libo = amount // 1000
    libo_sukli = amount % 1000

    five_h = libo_sukli // 500
    five_sukli = amount % 500

    two_h = five_sukli // 200
    two_sukli = amount % 200

    one_h = two_sukli // 100
    one_sukli = amount %  100

    five_t = one_sukli // 50
    five_sukli = amount % 50

jvp = True
while jvp == True:
    print("WELCOME TO MY BANK SIMULATOR PROGRAM")
    print("======================================")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Balance")
    print("4. Withdraw")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("CREATE ACCOUNT")
        print("PLEASE PROVIDE THE FOLLOWING INFORMATION")
        fullname = input("Enter your name: ")
        print("MUST PROVIDE INITIAL DEPOSIT")
        amount = eval(input("Enter your amount for your initial deposit: "))
        create_account(fullname, amount)

    elif choice == "2":
        print("============== DEPOSIT =============")
        amount = eval(input("Enter your amount: "))
        deposit(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        print("============ WITHDRAW =============")
        amount = eval(input("Enter the amount: "))
        withdraw(amount)

    elif choice == "5":
        print("Thank you for stopping by")

    else:
        break
    
>>>>>>> afb4775 (Initial commit)
