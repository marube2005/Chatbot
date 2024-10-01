#collect the neccessary inputs: principle(loan amount), apr (annual interest rate) , years.
#Calculate the monthly payment.

def main():
    print("This is a Monthly Payment loan calculator")
    print("")

    principal = float(input("Input the loan amount?"))
    annual_interest_rate = float(input("Input the annual interest rate :"))
    years = int(input("Input the number of years the loan was borrowed for:?"))

    monthly_interest_rate = annual_interest_rate/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate)** (-amount_of_months))

    print("Your monthly payis : %.2f" %(monthly_payment))

main()

    