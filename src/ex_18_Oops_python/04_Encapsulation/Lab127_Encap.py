"""
Encapsulation:-
Bind the data variables with the methods.
Instance varaible / data variables can be accessed by the only methods.
Methods - Def function within the class.
Wrapping or binding the 'instance variables / data variables' with the methods - Encapsulation.

"""

class Car:

    def __init__(self,name, make, model):

        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"starting the car with the name-> {self.name}")
        print(f"starting the car with the make-> {self.make}")
        print(f"starting the car with the model-> {self.model}")


lambo = Car("lambo", "V6", "2023")

lambo.start_engine()

hector = Car("Hector", "V6", "2024")

hector.start_engine()