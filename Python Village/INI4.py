a =     ##insert number
b =     ##insert number

numbers = range(a, b+1)

sum = 0

for i in numbers:
    if i % 2 == 1:
        sum += i
        
print sum