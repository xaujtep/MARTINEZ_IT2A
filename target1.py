<<<<<<< HEAD
for x in range (1, 10):
    for y in range(1, x+1):
        print(x, end = " ")
    print()
=======
# for x in range (1, 10):
#     for y in range(1, x+1):
#         print(x, end = " ")
#     print()


# def greet(name,age):
#     print(f"My name is {name} and I'm already {age} years old")

# greet("Tep", 19)

# Global variable for tax rate
tax_rate = 0.08  # 8% tax

def calculate_total(item_prices, product_names):
    # Local variable to store the subtotal
    subtotal = 0  
    
    print("\nShopping Cart:")
    for name, price in zip(product_names, item_prices):
        print(f"{name}: ${price:.2f}")
        subtotal += price
    
    tax = subtotal * tax_rate
    
    total_cost = subtotal + tax

    print(f"\nThe total cost (including tax) is: ${total_cost:.2f}")

shopping_cart = []
product_names = []
print("Enter the names and prices of items in your shopping cart. Type 'done' to finish.")

while True:
    product_name = input("Enter product name (or 'done'): ")
    if product_name.lower() == 'done':
        break
    
    try:
        price = float(input(f"Enter price for '{product_name}': "))
        product_names.append(product_name)
        shopping_cart.append(price)
    except ValueError:
        print("Invalid input. Please enter a valid price.")

calculate_total(shopping_cart, product_names)
>>>>>>> afb4775 (Initial commit)
