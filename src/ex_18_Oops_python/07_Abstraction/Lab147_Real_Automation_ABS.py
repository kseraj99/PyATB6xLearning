# Importing Abstract Base Class (ABC) and abstractmethod decorator
from abc import ABC, abstractmethod

# Creating an abstract parent class
class BrowserManager(ABC):

    # Abstract method: child classes MUST implement this method
    @abstractmethod
    def start(self):
        pass

    # Normal method: child classes can use this directly (optional to override)
    def stop(self):
        print("Stop Command")


# Creating a child class that inherits from BrowserManager
class ChromeBrowser(BrowserManager):

    # Implementing the abstract method 'start'
    def start(self):
        print("We are starting the Chrome")


# Creating an object of the child class
obj = ChromeBrowser()

# Calling the implemented start() method
obj.start()

# Calling the inherited stop() method from the parent class
obj.stop()
