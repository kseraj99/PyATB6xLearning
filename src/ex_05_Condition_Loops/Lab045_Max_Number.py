"""
Find the maximum number between two.

Logic building-

user input-> two integer
output-> integer 1 ever greater, then find max number

"""


num1 = float(input("Enter first number:"))

num2 = float(input("Enter second number:"))

if num1 > num2:
    print(f"{num1} is max number")
else:
    print(f"{num2} is max number")