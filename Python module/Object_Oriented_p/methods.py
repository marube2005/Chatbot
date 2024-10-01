class Instructor:
    def __init__(self,name,age,gender):
        self.firstname = name
        self.age = age
        self.gender = gender
        self.online=False
#Subjectname will expect a string as an argument only.
    def teach(self,subjectname):  #Will bind with the object at that moment.
      print("Teaching. Hello I am " + self.firstname +". I teach " , subjectname, "Subject.")
student_1 = Instructor("Ritah","19","female")
print(student_1.age,student_1.gender,student_1.online)
student_1.teach("English")

student_2 =Instructor("Mike","21","male")
print(student_2.age)
student_3 = Instructor("Malcom","17","male")
print(student_3.online)