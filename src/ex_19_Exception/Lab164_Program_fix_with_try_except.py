"""
In python to deal any kind of exception we will use. try, except and finally block.

try:
    # code that may throw error
except:
    # handle the error
else:
    # runs only if no exception
finally:
    # always runs

"""
a = int(input("Enter a number:\n"))

b = int(input("Enter b number:\n"))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Error because of Zero div b != 0")
