def add(a,b):
    return a + b
def sub(a,b):
   return a - b
def mul(a,b):
   return a * b  
def div(a,b):
    return a / b

while True:
 print(" A. Addition")
 print(" B. Subtraction")
 print(" C. Multiplication")
 print(" D. Division")
 print(" E. Exit")

 operator = input("Choose a choice from A to E.")

 a = int(input("Enter first integer:"))
 b = int(input("Enter second integer:"))

 if operator.upper() == "A": 
    print(f"Your answer is: {add(a, b)}")
    
 elif operator.upper() == "B":
    print(f"Your answer is: {sub(a, b)}")
 elif operator.upper() == "C":
      print(f"Your answer is: {mul(a, b)}")
 elif operator.upper() == "D":
        print(f"Your answer is: {div(a, b)}")
 else:
    print("Already Exitted!")
    quit()

