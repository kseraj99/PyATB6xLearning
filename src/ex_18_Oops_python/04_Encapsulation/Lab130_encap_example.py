"""
Encapsulation:-
Hide the data members(class variable and Instance variable)
by using only the methods.
"""
"""
Protected : _ Members are intended for internal use within the class and its subclasses.

Private : __  Members are only accessible within the class they are defined in.


"""

class Car:

    def __init__(self):
        self.password = "seraj"
        self.__password_secure = "pass123"

    def nany(self):
        self.__password_secure = "1234"


obj_ref = Car()
print(obj_ref.password)

obj_ref.nany()