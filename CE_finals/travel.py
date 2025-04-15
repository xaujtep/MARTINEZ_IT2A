speed = eval(input("What is the speed of the vehicle in mph? "))
time = eval(input("How many hours has it traveled? "))

times = 1

print("\nDistance Traveled: ")
while times <= time:
    distance = speed * times
    print(f"{times} hour{'s' if times > 1 else ''} is {distance} miles")
    times += 1
  