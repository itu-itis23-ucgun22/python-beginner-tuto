condition = True
count = 0
print(count)
while condition == True and count < 5:
    print("it is true")
    count += 1
    
print(count)

items = [234,435,654,975,243]
for index,item in enumerate(items):
   
   if item == 435 or index == 4:
        continue
   print(item,index)
numbers = [28,508299,340803,2893]
for a , number in enumerate(numbers):
    if a == 1:
        break
    print(a,number)
    
for x in range(6,15):
    print(x)