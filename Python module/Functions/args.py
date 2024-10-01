# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments.
# you can name anything you want. The important thing is to have the asterick.
#tuples are ordered and uncahangable. to be succesful you need to change the Tuple to a list. example:
#   sender = list(args) by doing this you have converted the tuple to a list.
def product(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(product(6,8,10))