"""
Class-Blueprint
- Class is a user-defined data type which defines its properties and its methods.
- Attributes | Properties |Data variables
- Behavior | Methods(functions) |  Data members  | Member functions.

very important-every class has attributes and behaviour

"""

class Person:
    # Constructor (used to initialize object attributes)
    def __init__(self, name=None, id=None, age=None, email=None, height=None, gender=None, phone_no=None, address=None):
        self.name = name
        self.id = id
        self.age = age
        self.email = email
        self.height = height
        self.gender = gender
        self.phone_no = phone_no
        self.address = address

    # Behaviour / Methods
    def talk(self):
        print("I can talk")

    # Method with argument, no return value
    def sleep(self, name):
        print("I am a method")
        print(f"Sleep {name}")

    # Method with argument and return value
    def sleep2(self, name):
        print("I am a method")
        return f"{name} is sleeping"

    def walk(self):
        print("I am walking")


# Creating an object of Person class
# ObjectRec = ClassName()-> Object
greet = Person()

# Calling sleep method, it prints messages but returns None
print(greet.sleep("Seraj"))  # This will print the function output AND then print None because sleep() returns nothing

