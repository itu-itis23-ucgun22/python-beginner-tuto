def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I will date")

#closure
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
a = counter()
print(a())
print(a())
print(a())