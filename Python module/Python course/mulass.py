name,age,status = "Elvis", 21, "Single"
print("My name is:",str(name), "and I am", str(age)," years old . I am " ,str(status))
print()
#if you have more than one variable sharing the same value
#You can assign it this way 
# Bob = Tom = Mary = John = Charity = 25
name = "bob"
#print(len(name))
#print(name.find("o"))
#print(name.capitalize())
#print(name.upper() )
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("b"))
#print(name.replace("o", "e"))
#print(name*8)

#typecasting- ability to convert  datatype of a value  to another data type.
x = 4
y = 4.6
z = "5.0"
print(x,y,z*3)
int(y)
z = int(float(z))
print(x,int(y),z*3)