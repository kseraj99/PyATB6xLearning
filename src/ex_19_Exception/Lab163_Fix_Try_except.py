
try:
    a = int(input("Enter a number:\n"))

    b = int(input("Enter b number:\n"))
    c = a / b
    print(c)
except ValueError:
    print("Getting Value Error")
except ZeroDivisionError:
    print("Getting ZeroDivisionError")
finally:
    print("I will always execute")

