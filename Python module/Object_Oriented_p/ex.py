class Circle:
    pi = 3.142    #Class Object Atribute.
    def __init__(self,radius):
       self.radius = radius
    def get_circumference(self):
        circum = self.radius * 2 * self.pi
        return circum
    def get_area(self):
        area = self.radius * self.pi * self.radius
        return area
circle_1 = Circle(3.142)
print(circle_1.get_circumference())
print(circle_1.get_area())
