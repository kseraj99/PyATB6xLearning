
# Importing ABC (Abstract Base Class) and abstractmethod from abc module
from abc import ABC, abstractmethod

# Creating an abstract class Father that inherits from ABC
class Father(ABC):

    # Constructor to initialize the name attribute
    def __init__(self, name):
        self.name = name

    # Declaring an abstract method
    # Any subclass must implement this method
    @abstractmethod
    def Loan(self):
        pass


# Amit class inherits from Father and MUST implement the abstract method Loan
class Amit(Father):

    # Implementing the abstract method
    def Loan(self):
        print("I am giving the 50K loan!")


# Creating an object of Amit class
obj = Amit("Pankaj")

# Calling the Loan method
obj.Loan()
