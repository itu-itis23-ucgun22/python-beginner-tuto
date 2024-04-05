numbers = [12,24,36]

square_of_numbers = [ n**2 for n in numbers]
print(square_of_numbers)

square_of_numbers = []
for n in numbers:
    square_of_numbers.append(n**2)
print(square_of_numbers)

new = list(map(lambda n: n*n,numbers))
print(new)