# Problem 6 - Sum square difference
# Attemp Date: 06-11-2021 SAT
# ---------------------------
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and 
# the square of the sum is, 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ---------------------------

sum_of_square = 0
square_of_sum = 0
end_num = 100
for i in range(1,end_num + 1):
    sum_of_square += i**2
    square_of_sum += i

square_of_sum = square_of_sum**2
print("Sum of square is " + str(sum_of_square) + "; Square of sum is" + str(square_of_sum))
diff = square_of_sum - sum_of_square
print("The difference is " + str(diff))
