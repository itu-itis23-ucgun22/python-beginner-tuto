class Animal:
    def walk(self):
        print("walking")

class Dog(Animal):
    def __init__(self,name,age):
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