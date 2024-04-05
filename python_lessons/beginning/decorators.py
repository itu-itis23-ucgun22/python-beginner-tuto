
count = 0
def logtime(func):
    def wrapper():
        print("say")
        val = func()
        print("friends.")
      
        return val
    return wrapper




@logtime
def hello():
    print("hello")


hello()