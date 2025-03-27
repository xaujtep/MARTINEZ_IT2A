num = eval(input("Enter the number of petals: "))

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