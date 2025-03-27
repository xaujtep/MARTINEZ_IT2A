#June V. Padillo , BSCE-G017 , TTh 1:00 - 2:30


#define to compute the maturity value
def compute_compound_interest(p,r,t,n):
    #formula
    amount = p*(1+(r/n))**(n*t)
    return amount

#loop to continue the code unless they input no
while True:  
    try:
        #User input
        p = float(input("Enter the principle amount: "))
        r = float(input("Enter the annual interest rate: ")) / 100
        t = int(input("Enter the number of times interest is compounded per year: "))
        n = int(input("Enter the number of years: "))

    #If non-numeric values is inputted then repeat the input
    except ValueError:
        print("Use non-numeric values!")
    
    else:
        #Compute compound interest
        final_amount = compute_compound_interest(p, r, n, t)
        final = final_amount - p

        #Display
        print(f"The principal amount: ${p} ")
        print(f"The annual interest rate: {r}")
        print(f"The number of times interest is compounded per year: {t} ")
        print(f"The number of years: {n}")
        print(f"Interest earned: ${final}")
        print(f"The final amount after {n} years is: ${final_amount: .2f}")

        input_again = input("Do you want to calculate again? ").lower() #.lower for uppercase and lowercase of the user's input

        #IF-Else funtion
        if input_again != "yes":
            print("Thank you for using my Calculator!")
            break
  









