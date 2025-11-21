
# BaseTest class (Parent)
class BaseTest:
    # Protected variable
    _driver = "Chrome"

    def setup(self):
        print(f"Launching browser: {self._driver}")

    def teardown(self):
        print("Closing browser")


# LoginTest class (Child)
class LoginTest(BaseTest):

    def __init__(self, username):
        # Private variables
        self.__username = username


    # Getter method to access private username
    def get_user(self):
        return self.__username

    # Method to run the test
    def run_test(self):
        print(f"Running login test with user: {self.get_user()}")


# Creating object and executing tests
test = LoginTest("admin")

test.setup()
test.run_test()
test.teardown()

# In other way

"""

class BaseTest:
    _drive = "Chrome"

    def setup(self):
        print(f"Lunching the browser: {self._drive}")

    def teardown(self):
        print("Closing the browser")

class LoginTest(BaseTest):
    __username = "admin"
    __password = "pass123"

    def get_user(self):
        return self.__username


    def runtest(self):
        user = self.get_user()
        print(f"Running login test with user: {user}")


obj_ref = LoginTest()

obj_ref.setup()
obj_ref.runtest()
obj_ref.teardown()
"""