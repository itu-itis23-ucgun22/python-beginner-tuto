class Dog():
    def __init__(self,name,age):
        self.name = name 
        self.af = age

    def __gt__(self,other):
        return True if self.af > other.af else False


roger = Dog('Roger',9)
syd = Dog('syd',10) 

print(roger > syd)