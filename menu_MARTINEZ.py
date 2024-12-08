
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
