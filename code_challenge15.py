<<<<<<< HEAD
import os
isGo = True
nt = 0 

while isGo == True:
    ask = input("Do you wish to create more triangles (yes or no) ---> ")

    if ask.lower() == "no" :
        os.system("cls")
        print("Program is Terminated")
        break
    elif ask.lower() == "yes":
        os.system("cls")
        nt =+ 1
        for x in range(1,6):
            for r in range (1, nt + 1):
                for y in range(1, x + 1):
                    print("^", end = " ")
                for z in range(5, x, -1):
                    print(" ", end = " ")
                print(end= " ")
=======
import os

isGo = True
nt = 0 

while isGo == True:
    ask = input("Do you wish to create more triangles (yes or no) ---> ")

    if ask.lower() == "no" :
        os.system("cls")
        print("Program is Terminated")
        break
    elif ask.lower() == "yes":
        os.system("cls")
        nt =+ 1
        for x in range(1,6):
            for r in range (1, nt + 1):
                for y in range(1, x + 1):
                    print("^", end = " ")
                for z in range(5, x, -1):
                    print(" ", end = " ")
                print(end= " ")
>>>>>>> afb4775 (Initial commit)
            print()