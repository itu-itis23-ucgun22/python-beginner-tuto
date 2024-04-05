x1 = True

if x1:
    print("yes")
else:
    print( "no")

x2 = 2
if x2:
    print("yes")
else:
    print( "no")

x3 = 0
if x3:
    print("yes")
else:
    print( "no")

x4 = ""
if x4:
    print("yes")
else:
    print( "no")

x5 = "hey"
if x5:
    print("yes")
else:
    print( "no")

A = any([x1,x3])
B = all([x1,x3])

print(A,B)