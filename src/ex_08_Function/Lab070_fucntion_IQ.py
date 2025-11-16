"""
Write a program to sum of three numbers from the user input.
if user does not give any number, use default as 100, 200, 300.
"""

# Logic building
"""
step-1
i/p- int
o/p- int

step-2
return n1+n2+n3

step-3
write logic
"""

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
num3 = int(input("Enter the third number:\n"))

def sum_of_three_numbers(n1= 100, n2= 200, n3= 300):
    return n1+n2+n3

# we can call the function with one or two parameter
results = sum_of_three_numbers(num1, num2, num3)

print(results)

result1 = sum_of_three_numbers()
print(result1)