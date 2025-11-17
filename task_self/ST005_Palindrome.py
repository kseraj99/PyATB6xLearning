"""
Write a program to find the string is palindrome or not?
"""

# Take input from the user
input_str = input("Enter a string:\n")

# Reverse the string using slicing
reversed_str = input_str[::-1]

# Check if original string and reversed string are the same
if input_str == reversed_str:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
