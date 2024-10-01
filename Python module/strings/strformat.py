#str.format() = optional method that gives users 
#               more control when displaying output.

animal = input("What Animal would like to use")
item = input("Name any item.")

#print("The",animal , "Jumped over the" , item,)
# {} - These are what are known as format fields as they act as placeholders for variables and values.
# They work in order. Example:
print("The {} jumped over the {}".format(animal , item))
print("The {0} jumped over the {1}".format(animal, item))#Positional Arguments.
# Keyword argument must be followed by a value. Example:
print("The {item} jumped over the {animal}".format(animal="cow",item="fence"))#Keyword argument as the words cows and fence as values inside a key.

# How we can add some padding to a string when we display it.
name = "Elvis"
print("Hello my name is {}. I am in Campus".format(name))
#You add padding by inserting a colon at the string format then by how much padding space you require to leave. Example:
#print("Hello my name is {:17}. I am in Campus".format(name)) # < symbol is used to left align an item 
# while > is used to right align an item to add padding. if needed to centre align use the ^ sign.

#if you need to truncate a number then you can use the format specifier . Example:
pi = 3.14598
print("The number pi is {:.2f}".format(pi))