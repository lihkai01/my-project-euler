# Problem 2 - Even Fibonacci numbers
# Attemp Date: 05-11-2021 FRI
# ---------------------------
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
# ---------------------------

# Initialise variable
x = [1,2]
even = []

# Find out all the number in Fibonacci sequence
while x[-1] + x[-2] < 4000000:
    n = len(x)
    new_val = x[n-1] + x[n-2]
    x.append(new_val)

# Sort out the even number terms
for num in x:
    if num%2 == 0:
        even.append(num)

# Sum up the even values and output the answer
ans = sum(even)
print(ans)