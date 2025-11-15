"""
Match-case:
In match, there is no concept of break here.
Match will match the value whatever you mention with the case.
default is _.

"""

day = int(input("Enter the day:\n"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Input")