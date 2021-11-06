# Problem 5 - Smallest multiple
# Attemp Date: 06-11-2021 SAT
# ---------------------------
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ---------------------------
num = 2520
counter = 0
ans = True

while ans:
    for i in range(2,20):
        if num % i == 0:
            ans = True
            counter += 1
        else:
            num += 2520    # if the number not match try another 2520 value
            counter = 0
            break

    if counter >= 9:
        print(num)
        break    # break the while loop when the ans printed