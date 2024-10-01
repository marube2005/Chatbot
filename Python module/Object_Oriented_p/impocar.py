from car import Car

car_1 = Car("Ford", "Mustang",2023,"Green")
car_2 = Car("Mercedes", "MercedesBenz",2021,"Black")

car_1.wheels = 2

Car.wheels = 3
print(car_1.model)
print(car_2.color)
print(car_1.wheels)
print(car_2.wheels)