"""
Hybrid Inheritance:-
A mix of multiple and multilevel inheritance.

"""

class A:

    def a_method(self):
        print("A method")

class B:

    def b_method(self):
        print("B method")

class C(A,B):

    def c_method(self):
        print("C method")


obj = C()

obj.a_method()
obj.b_method()
obj.c_method()