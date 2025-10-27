"""
Write a program to take a user age and let him know
if he can go th club, let suppose his age is 21.
"""

# Login building formula
# Step1
"""
i/p- age, int
o/p- string (result-> can go to clud or not)
"""
# Step2- Rough login
"""
if age>21 print can go
if age<21 print can not go
"""
# Step3- write the logic

age = int(input("Enter the age: "))

if age <= 0 or age >=130:
    print("Enter a valid age")
else:
    if age> 21:
        print("yes, You can go to Clud")
    else:
        print("No, You can not go to Clud")

# Step4- check the edge cases
"""
we should consider edge cases such as-
Negative age or extremely high value- program will break
Non Numeric input - ABC
age which is not valid >130
"""



## Conditional Expressions

## Syntax
# if (condition1): # if condition1 is True
#     print ("yes")
# elif(condition2): # if condition2 is True
#     print("no")
# else: # otherwise
#     print("maybe")

## Code indentation-Python uses indentation to indicate a block of code.


# a = int(input("Enter your age:"))
#
# if a>18:
#     print("you are above the age of consent:")
#     print("Good for you")
#
# elif a<0:
#     print("you are entering an invalid age")
#
# elif a==0:
#     print("This is not a valid age")
#
# else:
#     print("You are below the age of consent")
#     print("It is not good for you")
#
# print("End the program")
#
#
# b = int(input("Enter your age"))
#
# if b>18:
#     print("Yes")
#
# else:
#     print("No")


# a = 22
# if (a>9):
#     print("Greater")
# else:
#     print("lesser")

## ----------------------------------------------

# # only if statement without else

# a = 10
# if (a>9):
#     print("Greater")

# print("Lesser")

### ------------------------------------------
# only else statement without if
# else cant not exist without if condition

# # else:
# #     print("Lesser")



###------------------------------------------------
## Multiple if statements

# a = 22
# if (a > 9):
#     print("Greater")

# if (a < 9):
#     print("lesser")

# if (a == 9):
#     print("Equals")


## ---------------------------------------------
# one if statement along with multiple elif
#
# a = 22
# b = int(input("Enter number to compare with 22 : "))
# if (a > b):
#     print("Greater")
#     if(10 == 10):
#         print("Equals 10 ")
#         if(20 == 10):
#             pass
#
# elif (a < b):       # elif can not exist without if
#     print("lesser")
# elif (a == b):      # elif can not exist without if
#     print("Equals")
# else:   # else is optional
#    print("God Knows!!!")


## --------------------------------------------------------
