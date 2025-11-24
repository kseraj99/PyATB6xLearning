"""
Abstraction:-
Hide the details and show what is required.

"""

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name):
        self.name = name
    # whenever we have abstract, we don't have buddy means incomplete!
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

obj = Dog("PP")
obj.sound()
