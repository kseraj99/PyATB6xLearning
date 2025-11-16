"""
Write a program to calculate the even and odd number.

"""

# def find_even_odd(num):
#     if num%2==0:
#         print(f"{num} is even number!")
#     else:
#         print(f"{num} is odd number!")
#
# find_even_odd(5)
# find_even_odd(6)

# Using lambda

num1 = int(input("Enter the number:\n"))

lam_even_odd = lambda num : "Even" if num%2==0 else "odd"

print(lam_even_odd(num1))