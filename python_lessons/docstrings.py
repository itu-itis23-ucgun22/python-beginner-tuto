"""ekgn"""


class Animal:
    def walk(self):
        print("walking...")

class Dog(Animal):
    """this is a dog features"""
    def __init__(self,name,age):
        """name and age are important"""
        self.ey = name
        self.ye = age 

    def bark(self):
        print("hav")

karabas = Dog("karabas",54)
karabas.bark()
print(karabas.ey)
print(karabas.ye)
print(karabas.bark())
print(karabas.walk())
print(help(Dog))