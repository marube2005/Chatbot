#Inheritance - ability to inherit the attributes or the methods features/properties to a newly created class.
#The parent class is known as base/parent/super class while the child is known as the derived/child class
#Why Inheritance - Reduces data redundancy. Also mantains readability, accountability e.t.c
# The child class can have it's own unique properties. It's main purpose is to increase code re-usability.
#The child class can also have it's own implementation - You can redefine a method.(Method Overriding)
class Human:
    def __init__(self,num_heart) -> None:
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print("I can eat.")
    def walk(self):
        print("I can walk.")

class Male(Human):
    def __init__(self,name,num_heart) -> None:
       super().__init__(num_heart) #It is compulsory to access all the methods and attributes in the base class. Used when one has defined his own unit function.
       self.first_name = name 
    def flirt(self):
        print("I can flirt.")
    def walk(self):
        super().walk() # Will give you access to both the methods and attributes in the base class with the help of the function super() .
        print("I can run and drive.")
    def display(self):
        print(f"Hi, I am {self.first_name} and I have {self.num_heart} heart")
male_1 = Male("Malcom",1)
print(male_1.num_eyes)
print(male_1.first_name)
#male_1.eat()
male_1.walk()
#male_2 = Male()
#male_2.flirt()
#print(male_2.num_nose)
print(male_1.num_heart)
print(male_1.display())