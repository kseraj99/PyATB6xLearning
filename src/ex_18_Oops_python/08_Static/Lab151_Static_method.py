class Utility:

    def __init__(self):
        self.name = None

    @staticmethod
    def greet(name):
        print(f"Hi, {name}")

    def greet_personal(self, name):
        # store the name in the object
        self.name = name
        print(f"Hi, {self.name}")


obj = Utility()

# Calling static method
obj.greet("seraj")

# Calling personal greeting (updates object's name)
obj.greet_personal("Soname")

