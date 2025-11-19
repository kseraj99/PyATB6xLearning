
class Dog:

    name = None
    bread = None
    height = None
    weight = None

    def bark(self):
        print("Barking")
        print(self.name)

chow = Dog()
"""
Here 
Dog() is an object
chow is an object ref

imp- object ref can access all the method inside the class.

"""

print(chow.bark())