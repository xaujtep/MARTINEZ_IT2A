<<<<<<< HEAD
#input name and chosen number

name = input("Enter your name: ")
num = eval(input("Enter a number: "))

ans = num % 2

if ans == 0:
    print(f"Hi, {name}, {num} is an EVEN number")

    if num % 5 == 0:
        print(f"{num} is divisible by 5 but not in 9")
    elif num % 9 == 0:
        print(f"{num} is divisible by 9 but not in 5")
    elif num % 5 == 0 and num % 9 == 0:
        print(f"{num} is divisible by 5 and 9")
        
else:
    print(f"Hi, {name}, {num} is an ODD number")
=======
#input name and chosen number

name = input("Enter your name: ")
num = eval(input("Enter a number: "))

ans = num % 2

if ans == 0:
    print(f"Hi, {name}, {num} is an EVEN number")

    if num % 5 == 0:
        print(f"{num} is divisible by 5 but not in 9")
    elif num % 9 == 0:
        print(f"{num} is divisible by 9 but not in 5")
    elif num % 5 == 0 and num % 9 == 0:
        print(f"{num} is divisible by 5 and 9")
        
else:
    print(f"Hi, {name}, {num} is an ODD number")
>>>>>>> afb4775 (Initial commit)
