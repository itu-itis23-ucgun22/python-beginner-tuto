
#comparison_operators
a = 45
b = 54 

a < b
a >b
a ==b
a !=b
a>=b

#arithmetic operators
1 + 1
1 * 3
1 / 4
1 - 45 
5 % 3 #2 remainder
5 ** 3 #125
5 // 3 #it divides and round down

age = 8 
age += 5 #age = 13

#boolean operators
condition1 = True
condition2 = False

not condition1 #false
condition1 or condition2 #true
condition1 and condition2 #false

print(False or 'hey')
print(True or False)
print(0 or 1)
print('hi' or 'hey')
print([] or False)
print(False or [])
#if the first value is true it takes first else if the both of them are wrong it takes in the end.
print()
print()
print(False and 'hey')
print(True and False)
print(0 and 1)
print('hi' and 'hey')
print([] and False)
print(False and [])

# & performs AND
# | perfroms OR
# ^ performs XOR
#  ~ perform NOT
# >> performs shift right operation
# << performs shift left operation


def age():
    if age > 18:
        return True
    else: 
        return False
    
def age2():
    return False if age > 18 else True
  
  
