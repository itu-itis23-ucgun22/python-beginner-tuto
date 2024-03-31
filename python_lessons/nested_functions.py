def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I will date")

def count():
    count = 0
    def increment():
        nonlocal count 
        count +=1
        print(count)
    increment()

count()