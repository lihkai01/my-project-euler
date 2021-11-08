# Problem 7 - The 10001 Prime Number
# Attemp Date: 08-11-2021 MON
# ---------------------------
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# ---------------------------
import math

# Function for checking prime number (Function from Problem 5)
def checkPrime(factor):
    fac_list = []
    isPrime = False
    for j in range(1,math.ceil(math.sqrt(factor))+1):
        if (factor % j) == 0:
            fac_list.append(j)

    if len(fac_list) == 1:
        isPrime = True
    
    return isPrime

upper_limit = 10001
counter = 0
current_value = 2
while counter < upper_limit-1:
    if checkPrime(current_value):
        counter += 1
    
    current_value += 1

print(current_value-1)