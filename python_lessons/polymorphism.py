class Dog():
    def eat(self):
        print("dog eating")

class Cat():
    def eat(self):
        print("cat eating")


animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

Dog().eat()