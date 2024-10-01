#scope = The region that a variable is recognized.
#        A variable is only available from the scope inside the region it is declared.
#        A global and local scope of a variable can be created. Example:

# global variable is declared outside all other functions i.e it is available within all functions. Example:
name = "Elvis" # is an example of a global scope.
def my_name():
    name ="Marube" #Local scope because it is only visible from within this function.
    print(name)
my_name()

print(name),
#legb = local      global then built-in variables in that order.