#arguments - arguments preceded by an identifier when we pass them to a function.
#            The order of the arguments doesn't matter, unlike positional arguments
#            Python knows the name of the argument that our function receives.
#In the example below the order doesn't matter.
#def names(first,middle,last):
   # print("Hello",first,middle,last)

#names(last="Sewe",first="Harry",middle="Mogire")

def addition(a,b):
  sum = a + b
  print("Sum of",a,"and",b,"=",sum)

addition(b=7,a=9)