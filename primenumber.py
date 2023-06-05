numbers = [1,3,4,10,15,21,27,22,13,11]
prime_numbers = []

for digit in numbers:
    for num in range(2, digit):
        if digit%num == 0:
            break
    else:
        prime_numbers.append(digit)
        
print(prime_numbers)            