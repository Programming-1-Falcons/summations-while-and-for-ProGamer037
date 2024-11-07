number = int(input("Enter a number: "))
sum_while = 0
current = 1

while current < number:
    sum_while += current
    current += 1
    
print("Sum: ", sum_while + number)