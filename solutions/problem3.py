# Problem 3 - Largest prime factor
# Attemp Date: 05-11-2021 FRI
# ---------------------------
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# ---------------------------
import math

factor = []
prime_fac = []
x = 600851475143

# For loop for finding all the factor
num = math.ceil(math.sqrt(x))
for i in range(2,num):
    if (x % i) == 0:
        factor.append(i)
        corr = int(x/i)
        factor.append(corr)

# Function for checking prime number
def checkPrime(factor):
    fac_list = []
    isPrime = False
    for j in range(1,math.ceil(math.sqrt(factor))+1):
        if (factor % j) == 0:
            fac_list.append(j)

    if len(fac_list) == 1:
        isPrime = True
    
    return isPrime

# Check prime number in factor array
for value in factor:
    if checkPrime(value):
        prime_fac.append(value)

# output the maximum answer
print(max(prime_fac))