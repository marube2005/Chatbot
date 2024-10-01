temp = int(input("What is the temperature outside?"))

if not(temp >=10 and temp <= 25):
    print("Temperature is good today.")
    print("Go outside!")
elif not(temp < 10 or temp > 40):
    print("Temperature is not good today.")
    print("Stay inside!")
else:
    print("Temperature is moderate today")
    print("The decision is yours to stay inside or go outside.")
