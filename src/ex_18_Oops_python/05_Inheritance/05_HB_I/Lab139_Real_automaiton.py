
class BaseTest:

    def __init__(self, browser):
        self.browser = browser

    def setup(self):
        print(f"Lunching {self.browser}")

class LoginTest(BaseTest):

    def run_test(self):
        self.setup()
        print("Running login test....")

class SignupTest(BaseTest):

    def run_test(self):
        self.setup()
        print("Running signup Test......")


obj = LoginTest("Chrome")
obj.run_test()

obj = LoginTest("Firefox")
obj.run_test()
