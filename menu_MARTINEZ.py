<<<<<<< HEAD

import os

name = input("Enter your name: ")
print(f"Hi, {name}")
ans = input("Do you want to start the program (yes/no): ")

def challenge1():
    print("OUTPUT:")
    print("-----------------------")
    print("\n\t Hello, World!")
    print("\n\t Hi, Stephanie!")
    print("\n\t Good day, Sir, Leonard!")
    print("\n\t LOVE YOU, ZEN!")
    print("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b* * * * * * *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t\t\t\t*")
        
    print("\t PRINTING WITH INPUT")
    name = input("\t What is your name --->")
    print ("\t\t\t\t\t\t\t\t\t\t*\n\t\t\t\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b*  ""Hi!,"+name+"  *\n\t\t\t\t\t\t\t\t\t\t\b\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\b\b* * *\n\t\t\t\t\t\t\t\t\t\t*" )

def challenge2():
   pass
jvp = True

if ans.lower() == "yes":
    while jvp == True:
        print("1. PRINTING IN PYTHON ")
        print("2. VARIABLES IN PYTHON")
        print("3. CONDITIONAL STATEMENT")
        print("4. LOOPING STATEMENTS")
        print("5. FUNCTIONS")
        print("6. ARRAYS")
        print("7. DICTIONARY")
        print("8. EXIT")
        choice = input("Enter your choice: ")
        os.system('cls')

        if choice == "1":
            challenge1()
            break
        elif choice == "2":
            challenge2()
            break
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            pass
        else:
            break
else:
    print("Tnx")
=======

import os

#input for the user
name = input("Enter your name (CAPSLOCK ONLY): ").upper()
os.system('cls')
print("------------------------------------------------------------------")

print(f"\tGOOD DAY! {name}, WELCOME TO THE MAIN MENU SYSTEM. ")
print("------------------------------------------------------------------")
#if they wanted to use the program
ans = input("Do you want to start the program (yes/no): ")
os.system('cls')

print("==================================================================")

#menu for each topics
def menu_print():
    print("------------------- MENU FOR PRINTING ---------------------")
    print("\n\t\t1. SIMPLE PRINTING")
    print("\t\t2. PRINTING WITH STRINGS AND CONCATENATION")
    print("\t\t0. BACK TO MAIN MENU")

def menu_variables():
    print("------------------- MENU FOR VARIABLES ---------------------")
    print("\n\t\t1. PYTHON VARIABLES")
    print("\t\t2. VARIABLE NAMES")
    print("\t\t3. OUTPUT VARIABLES")
    print("\t\t4. PLUS AND CONCATENATION")
    print("\t\t0. BACK TO MAIN MENU")

def menu_condition():
    print("------------------- MENU FOR CONDITION ---------------------")
    print("\t\t1. FORTUNE COOKIES")
    print("\t\t2. I LOVE YOU REARRANGE")
    print("\t\t0. BACK TO MAIN MENU")

def menu_looping():
    print("------------------- MENU FOR LOOP ---------------------")
    print("\n\t\t1. FOR LOOP")
    print("\t\t2. FOR LOOP TRAINGLE")
    print("\t\t3. FOR LOOP MULTIPLICATION")
    print("\t\t4. WHILE LOOP")
    print("\t\t5. FOR LOOP WITH WHILE LOOP")
    print("\t\t0. BACK TO MAIN MENU")

def menu_function():
    print("------------------- MENU FOR FUNCTION ---------------------")
    print("\n\t\t1. SIMPLE FUNCTION")
    print("\t\t2. ARGUMENTS")
    print("\t\t3. PARAMETER")
    print("\t\t4. RETURN")
    print("\t\t0. BACK TO MAIN MENU")

def menu_scope():
    print("------------------- MENU FOR SCOPE ---------------------")
    print("\n\t\t1. WHAT IS GLOBAL AND LOCAL")
    print("\t\t2. GLOBAL AND LOCAL SCOPE EXAMPLE ")
    print("\t\t0. BACK TO MAIN MENU")

def menu_set():
    print("------------------- MENU FOR SETS ---------------------")
    print("\n\t\t1. WHAT IS SETS?")
    print("\t\t2. EXAMPLE FOR SETS")
    print("\t\t0. BACK TO MAIN MENU")

def menu_arrays():
    print("------------------- MENU FOR ARRAY ---------------------")
    print("\n\t\t1. SIMPLE ARRAY")
    print("\t\t2. LENGTH OF AN ARRAY")
    print("\t\t3. LOOPING ARRAY")
    print("\t\t4. ARRAY METHODS")
    print("\t\t5. INDEXING")
    print("\t\t6. SORTING ARRAY")
    print("\t\t0. BACK TO MAIN MENU")

def menu_dictionary():
    print("------------------- MENU FOR DICTIONARY ---------------------")
    print("\n\t\t1. ACCESSING ITEMS")
    print("\t\t2. UPDATING VALUE")
    print("\t\t3. EXAMPLE CODE FOR DICTIONARY")
    print("\t\t0. BACK TO MAIN MENU")

def menu_compileinonecode():
    print("------------------- ONE CODE FOR ALL OF THE TOPICS ---------------------")
    print("\n\t\t1. OPEN THE EXAMPLE")
    print("\t\t0. BACK TO MAIN MENU")

#function to use for the code of each topic
def printing_one():
    print("OUTPUT:")
    print("------------------------------------------------------------")
    print("\n\t Hello, World!")
    print("\n\t Hi, Stephanie!")
    print("\n\t Good day, Sir, Leonard!")
    print("\n\t LOVE YOU, ZEN!")

    print('''
INPUT:
------------------------------------------------------------
        print(" Hello, World!")
        print(" Hi, Stephanie!")
        print(" Good day, Sir, Leonard!")
        print(" LOVE YOU, ZEN!")
        print(" LOVE YOU, JP! ")
          ''')
    
def printing_two():
    print("OUTPUT:")
    print("------------------------------------------------------------")
    v1 = "But first, "
    v2 = "Coffee!"      
    print("\n\tWelcome to,", v1 + v2)

    print('''
INPUT:
------------------------------------------------------------
        v1 = "But first, "
        v2 = "Coffee!"      
        print("Welcome to,", v1 + v2)
          ''')

def variables_1():
    print("OUTPUT:")
    print("------------------------------------------------------------")
    
    x = 3
    y = "Steph"
    print(x)
    print(y)

    print('''
INPUT:
------------------------------------------------------------
        x = 3
        y = "Steph"
        print(x)
        print(y)
          ''')
    
def variables_2():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    myname = "Stephanie"
    friendname = "Yuzen"
    bfname = "Jp"
    mysurname = "Martinez"

    print(myname)
    print(friendname)
    print(bfname)
    print(mysurname)

    print('''
INPUT: 
------------------------------------------------------------
        myname = "Stephanie"
        friendname = "Yuzen"
        bfname = "Jp"
        mysurname = "Martinez"

        print(myname)
        print(friendname)
        print(bfname)
        print(mysurname)
          ''')


def variable_3():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    a = "Living"
    b = "so"
    c = "good!"
    print(a, b, c)

    print('''
INPUT: 
------------------------------------------------------------
        a = "Living"
        b = "so"
        c = "good!"
        print(a, b, c)
          ''')

def variable_4():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    v1 = "But first, "
    v2 = "Coffee"      
    print("\n\t Welcome to ", v1 + v2)

    print('''
INPUT:
------------------------------------------------------------
        v1 = "But first, "
        v2 = "Coffee"      
        print("\n\t Welcome to ", v1 + v2)
          ''')
    
def fortune_cookies():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    print("\n\tILL READ YOU, YOUR FORTUNE COOKIES")
    RN = eval(input("\n\tPick a randon number 1 through 10: "))
    if RN == 1:
        print("\n\tDo not be afraid of competition.")
    elif RN == 2:
        print("\n\tAn exciting opportunity lies ahead of you")
    elif RN == 3:
        print("\n\tStay healthy. Walk a mile")
    elif RN == 4:
        print("\n\tYou'll smile today!")
    elif RN == 5:
        print("\n\tParadise is always where love dwells.")
    elif RN == 6:
        print("\n\tTrue love is not something that comes everyday, follow your heart, it knows the right answer.")
    elif RN == 7:
        print("\n\tReach for joy and all else will follow.")
    elif RN == 8:
        print("\n\tForget injuries; never forget kindnesses.")
    elif RN == 9:
        print("\n\tYou are wise beyond your years.")
    else:
        print("\n\tBecareful some misfortune is awaiting for you")

    print('''
INPUT: 
------------------------------------------------------------
        print("ILL READ YOU, YOUR FORTUNE COOKIES")
        RN = eval(input("Pick a randon number 1 through 10: "))
        if RN == 1:
            print("Do not be afraid of competition.")
        elif RN == 2:
            print("An exciting opportunity lies ahead of you")
        elif RN == 3:
            print("Stay healthy. Walk a mile")
        elif RN == 4:
            print("You'll smile today!")
        elif RN == 5:
            print("Paradise is always where love dwells.")
        elif RN == 6:
            print("True love is not something that comes everyday, follow your heart, it knows the right answer.")
        elif RN == 7:
            print("Reach for joy and all else will follow.")
        elif RN == 8:
            print("Forget injuries; never forget kindnesses.")
        elif RN == 9:
            print("You are wise beyond your years.")
        else:
            print("Becareful some misfortune is awaiting for you")
          ''')

def ily_arrange():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    I = 1
    YOU = 2
    LOVE = 3

    print("\n\tYou can arrange the following word by using the corresponding number:")
    print("\n\tI = 1")
    print("\tYOU = 2")
    print("\tLOVE = 3")
    print("\n\t--------------------------------------------------------")
    word = int(input("\n\twhat do you think is the sequence?:"))
    if word == 123:
        print("\n\tI YOU LOVE",)
    elif word == 132:
        print("\n\tI LOVE YOU")
    elif word == 231:
        print("\n\tYOU LOVE I")
    elif word == 213:
        print("\n\tYOU I LOVE")
    elif word == 312:
        print("\n\tLOVE I YOU")
    elif word == 321:
        print("\n\tLOVE YOU I")
    else: 
        print("\n\tI DON'T LOVE YOU")

    print('''
INPUT: 
------------------------------------------------------------
        I = 1
        YOU = 2
        LOVE = 3

        print("You can arrange the following word by using the corresponding number:")
        print("I = 1")
        print("YOU = 2")
        print("LOVE = 3")
        print("--------------------------------------------------------")
        word = int(input("what do you think is the sequence?:"))
        if word == 123:
            print("I YOU LOVE",)
        elif word == 132:
            print("I LOVE YOU")
        elif word == 231:
            print("YOU LOVE I")
        elif word == 213:
            print("YOU I LOVE")
        elif word == 312:
            print("LOVE I YOU")
        elif word == 321:
            print("LOVE YOU I")
        else: 
            print("I DON'T LOVE YOU")
          ''')

def for_loop():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    for x in range (0,10):
        for y in range (0, x):
            print("*", end = " ")
        for z in range (x,10):
            print(" ", end = " ")
        print()

    print('''
INPUT:
------------------------------------------------------------
        for x in range (0,10):
            for y in range (0, x):
                print("*", end = " ")
            for z in range (x,10):
                print(" ", end = " ")
            print()
          ''')
    
def loop_triangle():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    for x in range(1, 6):
        for y in range(5, x, -1):
            print(" ", end = " ")
        for z in range(1, 2 * x):
            print("*", end = " ")
        print()  

    # Arrow head down
    for x in range(4, 0, -1):
        for y in range(5, x, -1):
            print(" ", end = " ")
        for z in range(1, 2 * x):
            print("*", end = " ")
        print()  

    print('''
INPUT: 
------------------------------------------------------------
        for x in range(1, 6):
            for y in range(5, x, -1):
                print(" ", end = " ")
            for z in range(1, 2 * x):
                print("*", end = " ")
            print()  

    # Arrow head down
        for x in range(4, 0, -1):
            for y in range(5, x, -1):
                print(" ", end = " ")
            for z in range(1, 2 * x):
                print("*", end = " ")
            print()  
          
          ''')

def loop_mult():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    num = eval(input("ENTER NUMBER OF COLUMNS: "))

    for x in range(1, 11):
        for y in range (1, num + 1):
            print(x*y, end = "\t")

        print()

    print('''
INPUT:
------------------------------------------------------------
        num = eval(input("ENTER NUMBER OF COLUMNS: "))

        for x in range(1, 11):
            for y in range (1, num + 1):
                print(x*y, end = "\t")

            print()
          
          ''')
    
def while_loop():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    loan_amount = float(input("Enter the loan amount: "))
    loan_period_years = int(input("Enter the loan period in years: "))

    annual_interest_rate = 0.03  
    months_in_year = 12
    monthly_interest_rate = annual_interest_rate / months_in_year  # Monthly interest rate

    total_months = loan_period_years * months_in_year

    monthly_principal = loan_amount / total_months

    remaining_loan = loan_amount
    month = 1

    print("\nPayment Schedule")
    print(f"{'Month':<7} {'Monthly Payment':<17} {'Interest':<12} {'Principal':<12} {'Remaining Loan'}")
    print("-----------------------------------------------------------------------")

    while month <= total_months:
        
        interest = remaining_loan * monthly_interest_rate
        
        monthly_payment = monthly_principal + interest
        
        remaining_loan -= monthly_principal
        
        if remaining_loan < 0:
            remaining_loan = 0.00

        print(f"{month: <10} ${monthly_payment:<15.2f} ${interest:<10.2f} ${monthly_principal:<10.2f} ${remaining_loan:.2f}")
        month += 1
        
    print('''
INPUT: 
        loan_amount = float(input("Enter the loan amount: "))
        loan_period_years = int(input("Enter the loan period in years: "))

        annual_interest_rate = 0.03  
        months_in_year = 12
        monthly_interest_rate = annual_interest_rate / months_in_year  # Monthly interest rate

        total_months = loan_period_years * months_in_year

        monthly_principal = loan_amount / total_months

        remaining_loan = loan_amount
        month = 1

        print("\nPayment Schedule")
        print(f"{'Month':<7} {'Monthly Payment':<17} {'Interest':<12} {'Principal':<12} {'Remaining Loan'}")
        print("-----------------------------------------------------------------------")

        while month <= total_months:
            
            interest = remaining_loan * monthly_interest_rate
            
            monthly_payment = monthly_principal + interest
            
            remaining_loan -= monthly_principal
            
            if remaining_loan < 0:
                remaining_loan = 0.00

            print(f"{month: <10} ${monthly_payment:<15.2f} ${interest:<10.2f} ${monthly_principal:<10.2f} ${remaining_loan:.2f}")
            month += 1
          
          ''')
    
def whilenloop():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    num = int(input("Enter the number of petals: "))

    current_petal = 0

    while current_petal <= num:
        for j in range(current_petal, num + 1):
            if j % 2 == 0:
                print(f"Petal {j}: He loves me! ")
            else: 
                print(f"Petal {j}: He loves me not! ")
            current_petal += 1

        if current_petal > num:
            break
    
    print('''
INPUT: 
------------------------------------------------------------
        num = int(input("Enter the number of petals: "))

        current_petal = 0

        while current_petal <= num:
            for j in range(current_petal, num + 1):
                if j % 2 == 0:
                    print(f"Petal {j}: He loves me! ")
                else: 
                    print(f"Petal {j}: He loves me not! ")
                current_petal += 1

            if current_petal > num:
                break
          ''')
def simple_func():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    def tep():
        print("You're so kind.")

    tep()
    tep()
    tep()

    print('''
INPUT: 
------------------------------------------------------------
        def tep():
            print("You're so kind.")

        tep()
        tep()
        tep()
          ''')
    
def argument():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    def greet(name,age):
        print(f"My name is {name} and I'm already {age} years old")

    greet("Tep", 19)

    print('''
INPUT:
------------------------------------------------------------
        def greet(name,age):
            print(f"My name is {name} and I'm already {age} years old")

        greet("Tep", 19)
          ''')
    
def example3():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    def whatif(pronoun, sentence):
        print(f"What if {pronoun} {sentence}.")

    whatif("he", "loves someone over me")
    whatif("she", "left because everything is tiring")
    whatif("she", "lost her passion")
    whatif("he", "give up")

    print('''
INPUT:
------------------------------------------------------------
        def whatif(pronoun, sentence):
            print(f"What if {pronoun} {sentence}.")

        whatif("he", "loves someone over me")
        whatif("she", "left because everything is tiring")
        whatif("she", "lost her passion")
        whatif("he", "give up")
          ''')

def returning():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    def tocomp(x):
        return 10 * x
    
    print(tocomp(8))
    print(tocomp(16))
    print(tocomp(24))

    print('''
INPUT: 
------------------------------------------------------------
        def tocomp(x):
            return 10 * x
        
        print(tocomp(8))
        print(tocomp(16))
        print(tocomp(24))

          ''')
    
def meaning():
   
    print('''
        Local Scope

            Variables defined within a function are considered to have local scope. 
        They are only accessible within that specific function. Once the function
        execution ends, thelocal variables are destroyed.
          
        Global Scope

            Variables defined outside of any function have global scope,
        which means they can be accessed from anywhere in the
        program, including inside functions.
          ''')
    
def globalandlocal():
    print("OUTPUT:")
    print("-------------------------------------------------------------------------------------------------------------")

    # Global variable for tax rate
    tax_rate = 0.08 

    def calculate_total(item_prices, product_names):
        # Local variable to store the subtotal
        subtotal = 0  
        
        print("\nShopping Cart:")
        for name, price in zip(product_names, item_prices):
            print(f"{name}: ${price:.2f}")
            subtotal += price
        
        tax = subtotal * tax_rate
        
        total_cost = subtotal + tax

        print(f"\nThe total cost (including tax) is: ${total_cost:.2f}")

    shopping_cart = []
    product_names = []
    print("Enter the names and prices of items in your shopping cart. Type 'done' to finish.")

    while True:
        product_name = input("Enter product name (or 'done'): ")
        if product_name.lower() == 'done':
            break
        
        try:
            price = float(input(f"Enter price for '{product_name}': "))
            product_names.append(product_name)
            shopping_cart.append(price)
        except ValueError:
            print("Invalid input. Please enter a valid price.")

    calculate_total(shopping_cart, product_names)

    print('''
INPUT:
-------------------------------------------------------------------------------------------------------------
        # Global variable for tax rate
        tax_rate = 0.08 

        def calculate_total(item_prices, product_names):
            # Local variable to store the subtotal
            subtotal = 0  
            
            print("\nShopping Cart:")
            for name, price in zip(product_names, item_prices):
                print(f"{name}: ${price:.2f}")
                subtotal += price
            
            tax = subtotal * tax_rate
            
            total_cost = subtotal + tax

            print(f"\nThe total cost (including tax) is: ${total_cost:.2f}")

        shopping_cart = []
        product_names = []
        print("Enter the names and prices of items in your shopping cart. Type 'done' to finish.")

        while True:
            product_name = input("Enter product name (or 'done'): ")
            if product_name.lower() == 'done':
                break
            
            try:
                price = float(input(f"Enter price for '{product_name}': "))
                product_names.append(product_name)
                shopping_cart.append(price)
            except ValueError:
                print("Invalid input. Please enter a valid price.")

        calculate_total(shopping_cart, product_names)
          
          ''')

def meaning_sets():
    print('''
        SETS
          
            Again with the Data structures or advanced variables, we have 
        something known as SETS. A set is a collection which is unordered and unindexed. 
        In Python, sets arewritten with curly brackets.
          
          ''')
    
def record():
    print("OUTPUT:")
    print("----------------------------------------------------------------------------------------")

    def record_keeping_app():
        data_store = set()  # Set to store unique key-value pairs as tuples
        
        while True:
            print("\nChoose an option:")
            print("a. Add Data")
            print("b. Delete Data")
            print("c. End")
            choice = input("Enter your choice (a/b/c): ").lower()
            
            if choice == 'a':
                # Add Data
                key = input("Enter Key: ")
                value = input("Enter Value: ")
                data_store.add((key, value))
                print("\nData Added Successfully!")
                print("Current Data:")
                for item in data_store:
                    print(item)
            
            elif choice == 'b':
                # Delete Data
                key_to_delete = input("Enter Key to Delete: ")
                found = False
                for item in list(data_store):  # Convert to list to allow removal
                    if item[0] == key_to_delete:
                        data_store.remove(item)
                        found = True
                if found:
                    print("\nData Deleted Successfully!")
                else:
                    print("\nKey not found!")
                print("Current Data:")
                for item in data_store:
                    print(item)
            
            elif choice == 'c':
                # End
                print("\nTHANK YOU")
                break
            
            else:
                print("\nInvalid choice! Please choose a, b, or c.")

    # Run the application
    record_keeping_app()

    print('''
INPUT: 
----------------------------------------------------------------------------------------
        def record_keeping_app():
            data_store = set()  # Set to store unique key-value pairs as tuples
            
            while True:
                print("\nChoose an option:")
                print("a. Add Data")
                print("b. Delete Data")
                print("c. End")
                choice = input("Enter your choice (a/b/c): ").lower()
                
                if choice == 'a':
                    # Add Data
                    key = input("Enter Key: ")
                    value = input("Enter Value: ")
                    data_store.add((key, value))
                    print("\nData Added Successfully!")
                    print("Current Data:")
                    for item in data_store:
                        print(item)
                
                elif choice == 'b':
                    # Delete Data
                    key_to_delete = input("Enter Key to Delete: ")
                    found = False
                    for item in list(data_store):  # Convert to list to allow removal
                        if item[0] == key_to_delete:
                            data_store.remove(item)
                            found = True
                    if found:
                        print("\nData Deleted Successfully!")
                    else:
                        print("\nKey not found!")
                    print("Current Data:")
                    for item in data_store:
                        print(item)
                
                elif choice == 'c':
                    # End
                    print("\nTHANK YOU")
                    break
                
                else:
                    print("\nInvalid choice! Please choose a, b, or c.")

        # Run the application
        record_keeping_app()
          
          ''')

def simple_array():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    grocery = ["apple","chicken","lemon","veggies"]
    print(grocery)

    print('''
INPUT: 
------------------------------------------------------------
        grocery = ["apple","chicken","lemon","veggies"]
        print(grocery)
          
          ''')
    
def length():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Medical Technologist"]
    x = len(dream)

    print(x)

    print('''
INPUT:
------------------------------------------------------------

        dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Medical Technologist"]
        x = len(dream)

        print(x)

          ''')
    
def looping_array():
    print("OUTPUT:")
    print("------------------------------------------------------------")

    Adj = ["Beautiful","Handsome","Cute"]
    Comment = ["Hi!","Why are you so","You look"]
    for x in Comment:
        for y in Adj:
            print("\n\t",x,y)

    print('''
INPUT: 
------------------------------------------------------------

        Adj = ["Beautiful","Handsome","Cute"]
        Comment = ["Hi!","Why are you so","You look"]
        for x in Comment:
            for y in Adj:
                print("\n\t",x,y)
          
          ''')
    
def method():
    print("OUTPUT:")
    print("----------------------------------------------------------------------------------------------------------------------------")

    dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Firefighter" , "Educator" , "Medical Technologist"]
    dream.pop(4)
    dream.insert(3, "Biologist")
    dream.append("House Wife")
    dream.remove('Educator')
    print(dream)

    print('''
INPUT:
----------------------------------------------------------------------------------------------------------------------------

        dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Firefighter" , "Educator" , "Medical Technologist"]
        dream.pop(4)
        dream.insert(3, "Biologist")
        dream.append("House Wife")
        dream.remove('Educator')
        print(dream)
          ''')

def indexing():
    print("OUTPUT:")
    print("----------------------------------------------------------------------------------------------------")

    dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Medical Technologist" , ""]
    print(f"I want to be an {dream [0]}")
    print(f"But I also want to be an {dream [2]}")

    print('''
INPUT:
----------------------------------------------------------------------------------------------------

        dream = ["Architect", "Engineer", "Nurse", "Radiologist", "Medical Technologist" , ""]
        print(f"I want to be an {dream [0]}")
        print(f"But I also want to be an {dream [2]}")
          
          ''')
    
def sorting():
    print("OUTPUT:")
    print("--------------------------------------------------------------------------------------")

    brands = ["Nike", "Adidas", "Puma", "AirJordan", "NewBalance","Converse"]
    sorted_brands = sorted(brands)
    print("Sorted brands:", sorted_brands)

    print('''
INPUT: 
--------------------------------------------------------------------------------------
        brands = ["Nike", "Adidas", "Puma", "AirJordan", "NewBalance","Converse"]
        sorted_brands = sorted(brands)
        print("Sorted brands:", sorted_brands)
          
          ''')

def accessing():
    print("OUTPUT:")
    print("---------------------------------------------------------------------------------------------------------------------------------------")

    dict =	{
    "name": "Stephanie",
    "course": "BSCE",
    "age": 19
    }

    print("My name is", dict ['name'])
    print("My age is", dict ['age'])
    print("My current course is", dict ['course'])
    print("My name is", dict ['name'], "I am", dict ['age'], "years old and I am currently a", dict ['course'], "student")

    print('''
INPUT:
---------------------------------------------------------------------------------------------------------------------------------------
        dict =	{
        "name": "Stephanie",
        "course": "BSCE",
        "age": 19
        }

        print("My name is", dict ['name'])
        print("My age is", dict ['age'])
        print("My current course is", dict ['course'])
        print("My name is", dict ['name'], "I am", dict ['age'], "years old and I am currently a", dict ['course'], "student")

          ''')
    
def updating():
    print("OUTPUT:")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")

    dict =	{
    "name": "Stephanie",
    "course": "BSCE",
    "age": 19
    }

    dict['course'] = "BSIT";
    dict['school'] = "DLL";

    print("My name is", dict ['name'], "I am", dict ['age'], "years old and I am actually currently a", dict ['course'], "student in", dict['school'])

    print('''
INPUT:
--------------------------------------------------------------------------------------------------------------------------------------------------------------
         dict =	{
        "name": "Stephanie",
        "course": "BSIT",
        "age": 19
        }

        dict['course'] = "BSIT";
        dict['school'] = "DLL";

        print("My name is", dict ['name'], "I am", dict ['age'], "years old and I am actually currently a", dict ['course'], "student in", dict['school'])

          ''')
    

def ex_dict():
    print("OUTPUT:")
    print("--------------------------------------------------------------------------------------------")

    def translate_to_bisaya(word, dictionary):
        return dictionary.get(word, "Translation not found")

    def add_translation(dictionary):
        tagalog_word = input("Enter the Tagalog word to add: ").lower()
        bisaya_translation = input("Enter the Bisaya translation: ").lower()
        if tagalog_word in dictionary:
            print("\nThis word already exists. Updating its translation...")
        dictionary[tagalog_word] = bisaya_translation
        print("\nNew translation added successfully!")

    def record_keeping_app():
        tagalog_to_bisaya = {  
            "kamusta": "kumusta",
            "salamat": "daghang salamat",
            "paalam": "padayon"
        }
        
        while True:
            print("\nChoose an option:")
            print("a. Translate to Bisaya")
            print("b. Add New Translation")
            print("c. View All Translations")
            print("d. End")
            choice = input("Enter your choice (a/b/c/d): ").lower()
            
            if choice == 'a':
                print("Choose here(available word to translate): ")
                print("kamusta")
                print("salamat")
                print("paalam")

                tagalog_word = input("Enter the Tagalog word to translate: ").lower()
                translation = translate_to_bisaya(tagalog_word, tagalog_to_bisaya)
                print(f"The Bisaya translation for '{tagalog_word}' is: {translation}")
                
                add_new = input("Do you want to add a new translation? (yes/no): ").lower()
                if add_new == 'yes':
                    add_translation(tagalog_to_bisaya)
            
            elif choice == 'b':
                add_translation(tagalog_to_bisaya)
            
            elif choice == 'c':
                print("\nCurrent Tagalog-to-Bisaya Translations:")
                for tagalog_word, bisaya_translation in tagalog_to_bisaya.items():
                    print(f"{tagalog_word} : {bisaya_translation}")
            
            elif choice == 'd':
                # End
                print("\nTHANK YOU")
                break
            
            else:
                print("\nInvalid choice! Please choose a, b, c, or d.")
    record_keeping_app()

    print('''
INPUT:
--------------------------------------------------------------------------------------------
        def translate_to_bisaya(word, dictionary):
            return dictionary.get(word, "Translation not found")

        def add_translation(dictionary):
            tagalog_word = input("Enter the Tagalog word to add: ").lower()
            bisaya_translation = input("Enter the Bisaya translation: ").lower()
            if tagalog_word in dictionary:
                print("\nThis word already exists. Updating its translation...")
            dictionary[tagalog_word] = bisaya_translation
            print("\nNew translation added successfully!")

        def record_keeping_app():
            tagalog_to_bisaya = {  
                "kamusta": "kumusta",
                "salamat": "daghang salamat",
                "paalam": "padayon"
            }
            
            while True:
                print("\nChoose an option:")
                print("a. Translate to Bisaya")
                print("b. Add New Translation")
                print("c. View All Translations")
                print("d. End")
                choice = input("Enter your choice (a/b/c/d): ").lower()
                
                if choice == 'a':
                    print("Choose here(available word to translate): ")
                    print("kamusta")
                    print("salamat")
                    print("paalam")

                    tagalog_word = input("Enter the Tagalog word to translate: ").lower()
                    translation = translate_to_bisaya(tagalog_word, tagalog_to_bisaya)
                    print(f"The Bisaya translation for '{tagalog_word}' is: {translation}")
                    
                    add_new = input("Do you want to add a new translation? (yes/no): ").lower()
                    if add_new == 'yes':
                        add_translation(tagalog_to_bisaya)
                
                elif choice == 'b':
                    add_translation(tagalog_to_bisaya)
                
                elif choice == 'c':
                    print("\nCurrent Tagalog-to-Bisaya Translations:")
                    for tagalog_word, bisaya_translation in tagalog_to_bisaya.items():
                        print(f"{tagalog_word} : {bisaya_translation}")
                
                elif choice == 'd':
                    # End
                    print("\nTHANK YOU")
                    break
                
                else:
                    print("\nInvalid choice! Please choose a, b, c, or d.")
        record_keeping_app()
          ''')
    
def final():
    print("OUTPUT:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

    def add_contact(contact_list):
        name = input("Enter contact name: ").strip() #strip is for removing the spaces at the beginning and at the end of string
        number = input("Enter contact number: ").strip()
        email = input("Enter contact email address: ").strip()
        

        contact_list[name] = {"Number": number, "Email": email}
        print(f"\nContact '{name}' added successfully!\n")


    def display_contacts(contact_list):
        print("\n--- Contact List ---")
        if not contact_list:
            print("No contacts found.")
        else:
            for name, details in contact_list.items():
                print(f"Name: {name}")
                print(f"Number: {details['Number']}")
                print(f"Email: {details['Email']}\n")


    def search_contact(contact_list):
        search_name = input("Enter the name of the contact to search: ").strip()
        if search_name in contact_list:
            print("\n--- Contact Found ---")
            print(f"Name: {search_name}")
            print(f"Number: {contact_list[search_name]['Number']}")
            print(f"Email: {contact_list[search_name]['Email']}\n")
        else:
            print("\nContact not found.\n")


    def edit_contact(contact_list):
        name_to_edit = input("Enter the name of the contact to edit: ").strip()
        if name_to_edit in contact_list:
            print("\n--- Edit Contact ---")
            new_number = input("Enter new contact number: ").strip()
            new_email = input("Enter new contact email address: ").strip()
            
            
            contact_list[name_to_edit] = {"Number": new_number, "Email": new_email}
            print(f"\nContact '{name_to_edit}' updated successfully!\n")
        else:
            print("\nContact not found.\n")


    def remove_contact(contact_list):
        name_to_remove = input("Enter the name of the contact to remove: ").strip()
        if name_to_remove in contact_list:
            del contact_list[name_to_remove]
            print(f"\nContact '{name_to_remove}' removed successfully!\n")
        else:
            print("\nContact not found.\n")


    def manage_contacts():
        def add_contact(contact_list):
            name = input("Enter contact name: ").strip()
            number = input("Enter contact number: ").strip()
            email = input("Enter contact email address: ").strip()
            

            contact_list[name] = {"Number": number, "Email": email}
            print(f"\nContact '{name}' added successfully!\n")


    def display_contacts(contact_list):
        print("\n--- Contact List ---")
        if not contact_list:
            print("No contacts found.")
        else:
            for name, details in contact_list.items():
                print(f"Name: {name}")
                print(f"Number: {details['Number']}")
                print(f"Email: {details['Email']}\n")


    def search_contact(contact_list):
        search_name = input("Enter the name of the contact to search: ").strip()
        if search_name in contact_list:
            print("\n--- Contact Found ---")
            print(f"Name: {search_name}")
            print(f"Number: {contact_list[search_name]['Number']}")
            print(f"Email: {contact_list[search_name]['Email']}\n")
        else:
            print("\nContact not found.\n")


    def edit_contact(contact_list):
        name_to_edit = input("Enter the name of the contact to edit: ").strip()
        if name_to_edit in contact_list:
            print("\n--- Edit Contact ---")
            new_number = input("Enter new contact number: ").strip()
            new_email = input("Enter new contact email address: ").strip()
            
            
            contact_list[name_to_edit] = {"Number": new_number, "Email": new_email}
            print(f"\nContact '{name_to_edit}' updated successfully!\n")
        else:
            print("\nContact not found.\n")


    def remove_contact(contact_list):
        name_to_remove = input("Enter the name of the contact to remove: ").strip()
        if name_to_remove in contact_list:
            del contact_list[name_to_remove]
            print(f"\nContact '{name_to_remove}' removed successfully!\n")
        else:
            print("\nContact not found.\n")


    def manage_contacts():
        contact_list = {} 
        
        while True:
            print("\n--- Contact List Menu ---")
            print("A. Add a new contact")
            print("B. Display all contacts")
            print("C. Search for a contact")
            print("D. Edit a contact")
            print("E. Remove a contact")
            print("F. Exit the program")
            
            choice = input("Choose an option: ").strip().upper()
            
            if choice == "A":
                add_contact(contact_list)
            elif choice == "B":
                display_contacts(contact_list)
            elif choice == "C":
                search_contact(contact_list)
            elif choice == "D":
                edit_contact(contact_list)
            elif choice == "E":
                remove_contact(contact_list)
            elif choice == "F":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")


    manage_contacts()
    
    print('''
INPUT: 
----------------------------------------------------------------------------------------------------------------------------------------------
        def add_contact(contact_list):
            name = input("Enter contact name: ").strip() #strip is for removing the spaces at the beginning and at the end of string
            number = input("Enter contact number: ").strip()
            email = input("Enter contact email address: ").strip()
            

            contact_list[name] = {"Number": number, "Email": email}
            print(f"\nContact '{name}' added successfully!\n")


        def display_contacts(contact_list):
            print("\n--- Contact List ---")
            if not contact_list:
                print("No contacts found.")
            else:
                for name, details in contact_list.items():
                    print(f"Name: {name}")
                    print(f"Number: {details['Number']}")
                    print(f"Email: {details['Email']}\n")


        def search_contact(contact_list):
            search_name = input("Enter the name of the contact to search: ").strip()
            if search_name in contact_list:
                print("\n--- Contact Found ---")
                print(f"Name: {search_name}")
                print(f"Number: {contact_list[search_name]['Number']}")
                print(f"Email: {contact_list[search_name]['Email']}\n")
            else:
                print("\nContact not found.\n")


        def edit_contact(contact_list):
            name_to_edit = input("Enter the name of the contact to edit: ").strip()
            if name_to_edit in contact_list:
                print("\n--- Edit Contact ---")
                new_number = input("Enter new contact number: ").strip()
                new_email = input("Enter new contact email address: ").strip()
                
                
                contact_list[name_to_edit] = {"Number": new_number, "Email": new_email}
                print(f"\nContact '{name_to_edit}' updated successfully!\n")
            else:
                print("\nContact not found.\n")


        def remove_contact(contact_list):
            name_to_remove = input("Enter the name of the contact to remove: ").strip()
            if name_to_remove in contact_list:
                del contact_list[name_to_remove]
                print(f"\nContact '{name_to_remove}' removed successfully!\n")
            else:
                print("\nContact not found.\n")


        def manage_contacts():
            def add_contact(contact_list):
                name = input("Enter contact name: ").strip()
                number = input("Enter contact number: ").strip()
                email = input("Enter contact email address: ").strip()
                

                contact_list[name] = {"Number": number, "Email": email}
                print(f"\nContact '{name}' added successfully!\n")


        def display_contacts(contact_list):
            print("\n--- Contact List ---")
            if not contact_list:
                print("No contacts found.")
            else:
                for name, details in contact_list.items():
                    print(f"Name: {name}")
                    print(f"Number: {details['Number']}")
                    print(f"Email: {details['Email']}\n")


        def search_contact(contact_list):
            search_name = input("Enter the name of the contact to search: ").strip()
            if search_name in contact_list:
                print("\n--- Contact Found ---")
                print(f"Name: {search_name}")
                print(f"Number: {contact_list[search_name]['Number']}")
                print(f"Email: {contact_list[search_name]['Email']}\n")
            else:
                print("\nContact not found.\n")


        def edit_contact(contact_list):
            name_to_edit = input("Enter the name of the contact to edit: ").strip()
            if name_to_edit in contact_list:
                print("\n--- Edit Contact ---")
                new_number = input("Enter new contact number: ").strip()
                new_email = input("Enter new contact email address: ").strip()
                
                
                contact_list[name_to_edit] = {"Number": new_number, "Email": new_email}
                print(f"\nContact '{name_to_edit}' updated successfully!\n")
            else:
                print("\nContact not found.\n")


        def remove_contact(contact_list):
            name_to_remove = input("Enter the name of the contact to remove: ").strip()
            if name_to_remove in contact_list:
                del contact_list[name_to_remove]
                print(f"\nContact '{name_to_remove}' removed successfully!\n")
            else:
                print("\nContact not found.\n")


        def manage_contacts():
            contact_list = {} 
            
            while True:
                print("\n--- Contact List Menu ---")
                print("A. Add a new contact")
                print("B. Display all contacts")
                print("C. Search for a contact")
                print("D. Edit a contact")
                print("E. Remove a contact")
                print("F. Exit the program")
                
                choice = input("Choose an option: ").strip().upper()
                
                if choice == "A":
                    add_contact(contact_list)
                elif choice == "B":
                    display_contacts(contact_list)
                elif choice == "C":
                    search_contact(contact_list)
                elif choice == "D":
                    edit_contact(contact_list)
                elif choice == "E":
                    remove_contact(contact_list)
                elif choice == "F":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please try again.\n")


        manage_contacts()
    
          ''')
    
jvp = True

if ans.lower() == "yes":
    while jvp == True:
        print("\n\tMAIN MENU")
        print("\n\t1. PRINTING")
        print("\t2. VARIABLES")
        print("\t3. CONDITIONAL STATEMENT")
        print("\t4. LOOPING STATEMENTS")
        print("\t5. FUNCTIONS")
        print("\t6. SCOPE")
        print("\t7. SETS")
        print("\t8. ARRAYS")
        print("\t9. DICTIONARY")
        print("\t10. FINAL OUTPUT")
        print("\t11. EXIT")
        choice = input("Enter your choice: ")
        os.system('cls')
        
        smd = True
        if choice == "1":
            while smd == True:
                menu_print()
                print_choice = input("Choose printing type: ")
                os.system('cls')

                if print_choice == "0":
                    break
                elif print_choice == "1":
                    printing_one()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif print_choice == "2":
                    printing_two()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')
        
        elif choice == "2":
            while jvp == True:
                menu_variables()
                variable_choice = input("Choose variable type: ")
                os.system('cls')

                if variable_choice == "0":
                    break
                elif variable_choice == "1":
                    variables_1()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif variable_choice == "2":
                    variables_2()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif variable_choice == "3":
                    variable_3()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif variable_choice == "4":
                    variable_4()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')

        elif choice == "3":
            while jvp == True:
                menu_condition()
                condition_choice = input("Choose the condition example: ")
                os.system('cls')

                if condition_choice == "0":
                    break
                elif condition_choice == "1":
                    fortune_cookies()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif condition_choice == "2":
                    ily_arrange()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')
                    
        elif choice == "4":
            while jvp == True:
                menu_looping()
                loop_choice = input("Choose the loop type: ")
                os.system('cls')

                if loop_choice == "0":
                    break
                elif loop_choice == "1":
                    for_loop()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif loop_choice == "2":
                    loop_triangle()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif loop_choice == "3":
                    loop_mult()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif loop_choice == "4":
                    while_loop()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif loop_choice == "5":
                    whilenloop()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')

        elif choice == "5":
            while jvp == True:
                menu_function()
                function_choice = input("Choose the function type: ")
                os.system('cls')

                if function_choice == "0":
                    break
                elif function_choice == "1":
                    simple_func()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                elif function_choice == "2":
                    argument()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                elif function_choice == "3":
                    example3()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                elif function_choice == "4":
                    returning()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                else:
                    print("INVALID OPTION")
                    os.system('cls')
                    
        elif choice == "6":
            while jvp == True:
                menu_scope()
                scope_choice = input("Choose the scope type: ")
                os.system('cls')

                if scope_choice == "0":
                    break
                elif scope_choice == "1":
                    meaning()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                elif scope_choice == "2":
                    globalandlocal()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                    
                else:
                    print("INVALID OPTION")
                    os.system('cls')
                    
        elif choice == "7":
            while jvp == True:
                menu_set()
                set_choice = input("Choose the set type: ")
                os.system('cls')

                if set_choice == "0":
                    break
                elif set_choice == "1":
                    meaning_sets()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif set_choice == "2":
                    record()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else: 
                    print("INVALID OPTION")
                    os.system('cls')

        elif choice == "8":
            while jvp == True:
                menu_arrays()
                array_choice = input("Choose the array type: ")
                os.system('cls')

                if array_choice == "0":
                    break
                elif array_choice == "1":
                    simple_array()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif array_choice == "2":
                    length()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif array_choice == "3":
                    looping_array()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif array_choice == "4":
                    method()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif array_choice == "5":
                    indexing()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif array_choice == "6":
                    sorting()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')

        elif choice == "9":
            while jvp == True:
                menu_dictionary()
                dict_choice = input("Choose the dictionary type: ")
                os.system('cls')

                if dict_choice == "0":
                    break
                elif dict_choice == "1":
                    accessing()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif dict_choice == "2":
                    updating()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                elif dict_choice == "3":
                    ex_dict()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("INVALID OPTION")
                    os.system('cls')

        elif choice == "10":
            while jvp == True:
                menu_compileinonecode()
                allcode = input("Choose the number you want to open: ")
                os.system('cls')

                if allcode == "0":
                    break
                elif allcode == "1":
                    final()
                    toback = input("Enter the keyword (type 'Good' to back): ")
                    os.system('cls')
                else:
                    print("Invalid")
                    os.system('cls')

        elif choice == "11":
            print("THANK YOU SO MUCH FOR YOUR VISIT. SMILE ALWAYS:>")
            break
        else:
            print("INVALID OPTION")
else:
    print("OKAY, THANK YOU HAVE A GOOD DAY!")





>>>>>>> afb4775 (Initial commit)
