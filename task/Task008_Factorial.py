"""
Factorial of a number is all positive integrals.
"""

num = int(input("Enter a number for which you want the factorial:\n"))

fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    if num == 0:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact *= i

    print(f"The factorial of {num} is {fact}")



