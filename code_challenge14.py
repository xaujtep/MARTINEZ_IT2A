num = True
sum = 0

while num == True:
    question = eval(input("Please enter a number: "))

    if question == 0:
        print("Loop Terminated")
        print(f"The sum of all the numbers is {sum}")
        break
    else:
        print("Please continue entering number")
        sum += question
        continue