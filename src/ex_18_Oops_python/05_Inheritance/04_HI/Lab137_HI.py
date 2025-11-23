
# Parent class (Base class)
class BaseTest:

    # Common setup method
    # This will be inherited by all child test classes
    def setup(self):
        print("Setup from BaseTest")


# Child class inheriting BaseTest
class LoginTest(BaseTest):

    # Child-specific method
    def run(self):
        print("Running login test")


# Another child class inheriting BaseTest
class SignupTest(BaseTest):

    # Child-specific method
    def run(self):
        print("Running Signup Test")


# Creating object of LoginTest and calling parent + child methods
LoginTest().setup()   # Inherited from BaseTest
LoginTest().run()     # Method of LoginTest

# Creating object of SignupTest and calling parent + child methods
SignupTest().setup()  # Inherited from BaseTest
SignupTest().run()    # Method of SignupTest
