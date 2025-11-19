"""
Constructor
- it is a special type of function
- Called automatically when you create an Object.
- Two Types
    - Default with no argument - DC
    - Parameterised - with argument - PC

- Constructor doesn't return anything
- __init__ name of the constructor.
- self-current Object, __init__

"""
class Dog:
    name = None
    bread = None
    height = None
    weight = None
    race = None

    def __init__(self, name, bread):
        print("Parameterized constructor")
        self.name = name
        self.bread = bread


    def bark(self):
        print("Barking")

    def sleep(self):
        print(f"who is sleeping-> {self.name} {self.bread}")

    def talk(self):
        pass

chow = Dog("chow", "mistif")

rancho = Dog("rancho", "desi")

chow.sleep()

rancho.sleep()
