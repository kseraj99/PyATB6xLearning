"""
Grade Calculater.
Write a program that calculates and displays the letter grade
for a given numerical score (e.g- A, B, C, D and F)
Based on the following grade-

A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: 0-59

"""


# Logic building formula

# Step1
"""
user input- score- integer
o/p will be string- A, B 
"""

score = int(input("Enter the score:"))

if score > 100 or score <= -1:
    print("You are Superman! you can not get the grade ❌")
else:
    if 90 <= score <= 100:
        print("Your grade is A")
    elif 80 <= score <= 90:
        print("Your grade is B")
    elif 70 <= score <= 80:
        print("Your grade is C")
    elif 60 <= score <= 70:
        print("Your score is D")
    else:
        print("your grade is F")
