#exception = events detected during execution that interrept the flow of a progrsm.
#Uses try and except , and Finally.
try:
 numerator = int(input("Enter a numbe to divide:"))
 denomenator = int(input("Enter the number to be divided by:"))
 result = numerator / denomenator
except ZeroDivisionError as e:
 print("Can't divide by zero. Please try again.")
 print(e)
except ValueError as e:
 print("Only numbers are allowed not strings.")
 print(e)
except Exception as e:
 print(" Something went wrong")
 print(e)
else:
 print(result)
finally:
 print("Till we meet again.") #whether or not the block of code encounters an error or not this block of code will be executed.