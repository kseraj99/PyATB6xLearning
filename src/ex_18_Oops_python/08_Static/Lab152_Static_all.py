"""
Static method:-
A static method is a method that belongs to a class rather than an
 instance of the class

"""

class O:

    @staticmethod
    def sum(a, b):
        return a+b

# static method can access directly.

print(O.sum(3,4))