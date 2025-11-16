"""
Checking for a leap year.
leap day occurs in each year that is a multiple of 4.
except the year evenly divisible by 100 but not by 400.

"""


def check_leap_year(year):
    if (year % 4 ==0 and year%100 != 0) or (year%400==0):
        return True
    else:
        return False


year = int(input("Enter a year:\n"))

if check_leap_year(year):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")




# In other way
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

"""




