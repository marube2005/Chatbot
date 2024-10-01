class Student:
    def __init__(self,name,age,gender):
        self.first_name = name
        self.age = age
        self.gender = gender
        self.online = False

student_1 = Student("Ritah","19","female")
print(student_1.first_name)
student_2 = Student("Mike","21","male")
print(student_2.age)
student_3 = Student("Malcom","17","male")
print(student_3.online)