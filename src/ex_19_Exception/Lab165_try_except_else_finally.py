try:
    a = int(input("Enter a number:\n"))

    b = int(input("Enter b number:\n"))
    c = a / b

except ValueError:
    print("Getting Value Error")
except ZeroDivisionError:
    print("Getting ZeroDivisionError")
else:
    print(c)
finally:
    print("I will always execute")