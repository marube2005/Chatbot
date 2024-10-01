#** kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept varying amount of keyword Dictionary.
#            similar to args.

def hello(**kwargs):
    #print("Hello", kwargs['first'], kwargs['last']) - If yoi wanna print all the names then you write like this:
    print("Hello"," ", end="")
    for key,value in kwargs.items():
        print(value," " ,end="")

hello(first = "Elvis", middle = "Xavier", last = "Marube")