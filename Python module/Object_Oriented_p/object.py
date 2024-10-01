#oop is a instance of a class.
# By use of programming we can create representationWe can make real life objects by assis of real life objects.
# It has attributes(what an object is or has.) like name,age,height e.t.c 
#Object is an instance of a class.
#methods - what an object can do. eg sleep,eat and make youtube videos.
#In order to achieve this we need to use classes (structure of an object)
#Processing object programming is used for short programmes. The steps in which we are going to perfom a task.(pop)
#In pop, we focus on functions not the data. Throw back is no data security as we are focused on functions.
#  i.e. Multiple functions updating global variables. # The functions have many relationships with each other.
#In built classes e.g. (int,str,bool). # In OOP, the functions are known as methods wile the variables are known as attributes coz they are associated with objects.
#In oop, we try to model real life objects that is modelled with help of attributes and methods(functions).
#Class os a blueprint(sketch,skeleton) of an object.
#In oop, the methods and attributes are not free floating. 
#An object refers to the combing of some piece of functionality and data.
#One class many objects. With classes, you can create objects.
#Class is a user defined datatype. The attributes and methods are associated with class and attached to the object.
#Oriented meaning our interest is in an 0bject.
#class Car:
 #   make = None
  #  model = None  Data is very important.
   # year = None
    #color = Non
#
#    def __init__(self) -> None:      # Special method which will construct objects for us.
 #       pass
#
#  def drive(self):                   #method
 #       print("This car is driving")

  #  def stop(self):                   #method
   #     print("This car is stopped")

class InstructorInfo:
  def __init__(self): 
    print("Creating a new object.")   # It will function when a new object is being created.
 #SELF IS REFERENCING the actual object. # Self will be instructor_1 and instructor_2 and instructor_3.
instructor_1 =InstructorInfo()
instructor_1.name = "Elvis"
instructor_1.last_name = "Marube"
instructor_1.age = 28
print(type(instructor_1))
print(instructor_1.name)

instructor_2 =InstructorInfo()
instructor_2.name = "Priyanka"
instructor_2.last_name = "Chopra"
instructor_2.age = 32
print(type(instructor_2))
print(instructor_2.name)

instructor_3 =InstructorInfo()
instructor_3.name = "Mahir"
instructor_3.last_name = "Musa"
instructor_3.age = 25
print(type(instructor_3))
print(instructor_3.name)