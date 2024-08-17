number = 1092
copy_of_number = number 
prime_factors = []

while number > 1:
    for i in range(2, copy_of_number+1):
        if number % i == 0:
            prime_factors.append(i)
            number = int(number / i)
            break

print(prime_factors)