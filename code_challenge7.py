<<<<<<< HEAD
#my details
Programmer = "Stephanie Martinez"
Course = "BSIT-2A"

#interface
print("PROGRAM: CASH REGISTER")
print(f"PROGRAMMER: {Programmer}")
print(f"COURSE: {Course}")
print("============================")

#input and calculating
buyG = input("Did you buy a grocery? (Yes/No): ")

if buyG.lower() == "yes":
	item_name = input("Name of the item: ")
	price = eval(input(f"Price of {item_name}: "))
	age = int(input("Customer age: "))
	amount_given = eval(input("Amount Given: "))
	print("===============================")

	tax_rate = 12.3 / 100 
	tax = price * tax_rate
	total_price = price + tax

	if age >= 60: 
		discount_rate = 5.2 / 100 
		discount = total_price * discount_rate
		total_price -= discount
	else:
		discount = 0
	
	change = amount_given - total_price


	print(f"Item Purchased: {item_name}")
	print(f"Price: {price: .2f}")
	print(f"Tax (12.3): {tax: .2f}")

	
	if age >= 60:
		print(f"Senior Discount (5.2): -{discount: .2f}")
	print(f"Total Price: {total_price: .2f}")
	print(f"Amount Given: {amount_given: .2f}")
	print(f"Change: {change: .2f}")
else: 
=======
#my details
Programmer = "Stephanie Martinez"
Course = "BSIT-2A"

#interface
print("PROGRAM: CASH REGISTER")
print(f"PROGRAMMER: {Programmer}")
print(f"COURSE: {Course}")
print("============================")

#input and calculating
buyG = input("Did you buy a grocery? (Yes/No): ")

if buyG.lower() == "yes":
	item_name = input("Name of the item: ")
	price = eval(input(f"Price of {item_name}: "))
	age = int(input("Customer age: "))
	amount_given = eval(input("Amount Given: "))
	print("===============================")

	tax_rate = 12.3 / 100 
	tax = price * tax_rate
	total_price = price + tax

	if age >= 60: 
		discount_rate = 5.2 / 100 
		discount = total_price * discount_rate
		total_price -= discount
	else:
		discount = 0
	
	change = amount_given - total_price


	print(f"Item Purchased: {item_name}")
	print(f"Price: {price: .2f}")
	print(f"Tax (12.3): {tax: .2f}")

	
	if age >= 60:
		print(f"Senior Discount (5.2): -{discount: .2f}")
	print(f"Total Price: {total_price: .2f}")
	print(f"Amount Given: {amount_given: .2f}")
	print(f"Change: {change: .2f}")
else: 
>>>>>>> afb4775 (Initial commit)
	print("No grocery purchase was made")