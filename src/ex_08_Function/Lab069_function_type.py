"""
Built-in function
user define function-
1. No return function/no parameter
2. return something
3. Parameter function
4. No parameter/arguments

"""

import math

result = max(3,5)

print(result)


# no return/no parameter

def greet():
    print("Hello World!")

greet()

# no return but arguments/parameter are there.

def greet_me(name):
    print(f"Hello {name}!")

greet_me("Seraj")

#no return but default parameter/arguments.

def greet_other(name= "Seraj"):
    print(f"Hello {name}!")

greet_other()
greet_other("Amit")

# Arguments + return type function

def sum_of_number(a,b):
    return a+b

result = sum_of_number(3,4)
print(result)