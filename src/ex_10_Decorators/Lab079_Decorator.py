"""
A decorator is something that:

👉 Takes a function as input
👉 Adds extra behavior to it (before or after the function runs)
👉 Returns the modified function

"""

"""
💡 What happens here?

add_security is a function that accepts another function (func) as an argument.

Inside it, wrapper() is a new function that adds extra steps:

Steps before func() executes

Steps after func() executes

func() is the actual function being decorated (like drive_ola_scooter)

return wrapper() means:

❗ Important:

Most decorators return wrapper, not wrapper().

But here you wrote wrapper(), which means:

✔ The wrapper function is executed immediately
✔ The result of wrapper() (which is None) replaces the original function

That’s why when your program runs, it prints everything immediately during decoration, 
not when the functions are called.

2️⃣ Using the decorator with @add_security
@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")


This is the same as writing:

drive_ola_scooter = add_security(drive_ola_scooter)


So:

drive_ola_scooter is passed into add_security

Inside the decorator, wrapper() runs immediately

Everything inside wrapper() is printed instantly

After that, the function name drive_ola_scooter becomes None

⭐ Final Summary (Very Easy Explanation)
✔ What is a decorator?

A function that wraps another function and adds extra behavior.

✔ What does add_security do?

It adds:

Instructions before riding the scooter

Instructions after riding the scooter

✔ What is unusual in your code?

You used:

return wrapper()


instead of:

return wrapper


👉 Because of this, the decorated functions run immediately at import time.

So when you run your program:

drive_ola_scooter() does NOT wait to be called

Its decorated version runs instantly

Same for drive_zyp_scooter()
"""


def add_security(func):

    def wrapper():
        print("1. Before the function is called!")
        print("2. Add Helmet, Dashboard, knee guard ")
        func()
        print("3. After the function is called!")
        print("4. Secure driving, leave all the items!")

    return wrapper()



@add_security
def drive_ola_scooter():
    print("I am driving ola scooter")


@add_security
def drive_zyp_scooter():
    print("Driving zyp scooter")