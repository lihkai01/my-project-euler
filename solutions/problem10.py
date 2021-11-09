# Problem 10 - Summation of primes
# Attemp Date: 09-11-2021 TUE
# ---------------------------
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# ---------------------------
import math

prime_number = [2]
# Function for checking prime number (From Problem 3)
def checkPrime(factor):
    fac_list = []
    for j in range(1,math.ceil(math.sqrt(factor))+1):
        if (factor % j) == 0:
            fac_list.append(j)

    if len(fac_list) == 1:
        prime_number.append(factor)

for i in range(3,2000000):
    checkPrime(i)

#print(prime_number)
print(sum(prime_number)) 

# This is not a good solution it takes 152.835 seconds to run
