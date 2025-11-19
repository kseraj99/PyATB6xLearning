class Home:

    def __init__(self):
        # Public variable — can be accessed from outside the class
        self.public_var = "Father"

        # Private variable — cannot be accessed directly from outside the class
        self.__private_var = "baby"

    def mom(self):
        """
        Public method that can be called from outside the class.
        It can access private variables and private methods inside the class.
        """
        print(self.__private_var)  # Accessing private variable

        self.__wife()  # Calling private method

    def __wife(self):
        """
        Private method — cannot be accessed directly using object reference.
        Only accessible inside the class.
        """
        print("private wife")


# Creating object of Home class
obj_ref = Home()

# Direct call to private method is not allowed — this will cause an error
# obj_ref.__wife()

# Calling public method which internally uses private variable and method
obj_ref.mom()
