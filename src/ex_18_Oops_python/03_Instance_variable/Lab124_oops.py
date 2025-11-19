a = 10 # variable which is available everywhere in the program.

class Person:

    b = 20 # This is the instance variable

    def print_info(self):
        c = 30 # It is a local variable
        print(c)
        print(self.b)
        print(a)


object_ref = Person()

object_ref.print_info()