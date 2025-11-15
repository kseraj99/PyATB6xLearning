"""
Modulus of 2 is not equal to zero will give you the odd number.
"""

for i in range(10):
    if i % 2 != 0:
        print(i)


# Another way to find the odd number

for num in range(10):
    if num % 2 == 0:
        continue
    else:
        print(num)