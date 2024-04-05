from functools import reduce

def double(a):
    return a *2 

numbers = [1,2,3] 
multiply = map(double,numbers)
print(list(multiply))

result = map(lambda a : a * a , numbers)

def iseven(n):
    return n % 2 == 0

print(list(filter(iseven,numbers)))



sum = 0
expenses = [('a',80),('b',120)]
sum = reduce(lambda x,y : x[1] + y[1],expenses)

print(sum)