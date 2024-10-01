age = int (input("How old are you?"))
if(age >= 18 & age <70):
    print("You  are able to drive a car")
elif(age >= 16 & age <18):
    print("You can go for driving classes")
elif(age < 0):
    print("Invalid age")
else: (
    print("You are not able to drive a car")
)