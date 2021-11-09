# Problem 9 - Special Pythagorean triplet
# Attemp Date: 08-11-2021 MON
# ---------------------------
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ---------------------------

for a in range(1,500):
    for b in range(1,500):
        c = 1000 - a - b
        if (a**2 + b**2 == c**2):
            ans = a * b * c
            #print(a,b,c)

print(ans)