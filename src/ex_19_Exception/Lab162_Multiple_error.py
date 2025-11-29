a = int(input("Enter a number:\n"))

b = int(input("Enter b number:\n"))
try:
    c = a/b
    print(c)
except (TypeError, NameError, ValueError, ZeroDivisionError):

    print("Error due to Type, name, value or Zero div!")
