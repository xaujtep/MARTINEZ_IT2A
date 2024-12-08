
# Arrow head up
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
