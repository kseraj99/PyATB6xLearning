"""
Find the maximum number between 3.

Logic building-

user input will be, num1, num2, and num3 - integer
o/p will be int or string with max number
"""

num1 = int(input("Enter the num1:"))

num2 = int(input("Enter the num2:"))

num3 = int(input("Enter the num3:"))


if num1 >= num2 and num1 >= num3:
    print(f"{num1} is maximum number")
if num2 >= num1 and num2 >= num3:
    print(f"{num2} is maximum number")
else:
    print(f"{num3} is maximum number")