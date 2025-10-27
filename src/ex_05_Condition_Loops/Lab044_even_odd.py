"""
Find the number is even or odd
"""

num = int(input("Enter the number: "))

if num >=0:
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
else:
    print(f"{num} is negative number")

