weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

bmi = (weight / (height**2)) * 703

print('Your BMI is', (format(bmi, '.2f')))

if bmi <=18.5:
    print("Underweight")
elif bmi >= 25:
    print("Overweight")
else:
    print("Normalweight")

