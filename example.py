# Loan Calculation Program with For and While Loops

loan_amount = float(input("Enter the loan amount: "))
loan_period_years = int(input("Enter the loan period in years: "))

annual_interest_rate = 0.03  
months_in_year = 12
monthly_interest_rate = annual_interest_rate / months_in_year  # Monthly interest rate

total_months = loan_period_years * months_in_year

monthly_principal = loan_amount / total_months

remaining_loan = loan_amount
month = 1

# Print Headers
print("\nPayment Schedule")
print(f"{'Month':<7} {'Monthly Payment':<17} {'Interest':<12} {'Principal':<12} {'Remaining Loan'}")
print("-----------------------------------------------------------------------")

while month <= total_months:
    
    interest = remaining_loan * monthly_interest_rate
    
    monthly_payment = monthly_principal + interest
    
    remaining_loan -= monthly_principal
    
    if remaining_loan < 0:
        remaining_loan = 0.00

    print(f"{month: <10} ${monthly_payment:<15.2f} ${interest:<10.2f} ${monthly_principal:<10.2f} ${remaining_loan:.2f}")
    month += 1