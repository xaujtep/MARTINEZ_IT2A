even_num =[]
odd_sum = 0

while True:

    user = int(input("Enter a number(Type 0 to stop): "))

    if user == 0:
        break
    elif user % 2 == 0:
        even_num.append(user)

    else:
        odd_sum += user

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_num}")