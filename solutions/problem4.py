# Problem 4 - Largest palindrome product
# Attemp Date: 06-11-2021 SAT
# ---------------------------
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# ---------------------------
import math

a = 100
b = 100
palindrome = []
# funtion to check palindrome
def checkPalindrome(value):
    isPalindrome = False
    num = value
    str_num = str(num)
    n = int(len(str_num))
    
    if (n == 6) & (str_num[2] == str_num[n-3]):
        if str_num[0] == str_num[n-1]:
            if str_num[1] == str_num[n-2]:
                isPalindrome = True
    elif (n == 5):
        if str_num[0] == str_num[n-1]:
            if str_num[1] == str_num[n-2]:
                isPalindrome = True

    return isPalindrome


# loop to count all product number
for i in range(a,999):
    for j in range(b,999):
        num = i*j
        if checkPalindrome(num):
            palindrome.append(num)

print(max(palindrome))
