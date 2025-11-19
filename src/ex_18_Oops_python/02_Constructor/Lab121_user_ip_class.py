
class Person:

    def __init__(self):
        print("Let's take the user input, please share the name, age, phone and occupation")

        self.name = input("Enter the name:\n")
        self.age = int(input("Enter the age:\n"))
        self.phone = int(input("Enter the phone number:\n"))
        self.occupation = input("Enter the occupation:\n")

    def display_values(self):
        print(f"My name is {self.name}, age is {self.age}, phone num is {self.phone} and occupation is {self.occupation}")


seraj = Person()
seraj.display_values()