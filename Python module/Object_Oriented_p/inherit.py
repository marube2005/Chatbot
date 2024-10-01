class Animal:

    alive = True
    def eat(self):
        print("This animal is eating now")
    def sleep(self):
        print("This animal is sleeping now")
    def play(self):
        print("This animal is playing now")
class Rabbit(Animal):
    def run(self):
        print("This Rabbit is running from us")
rabbit_1 = Rabbit()
rabbit_1.eat()
rabbit_1.run()

class Dog(Animal):
    def barking(self):
        print("This Dog is barking to a stranger")
dog_1 = Dog()
dog_1.sleep()
print(dog_1.alive)
dog_1.barking()


class Hawk(Animal):
    def fly(self):
        print("The Hawk has flown with the chick.")
hawk_1 = Hawk()
hawk_1.play()
hawk_1.fly()
