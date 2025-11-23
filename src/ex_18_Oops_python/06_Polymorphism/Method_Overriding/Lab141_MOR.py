
class TestSuite:

    def info(self):
        print("Running suite information")

class BaseTest(TestSuite):

    def setup(self):
        print("Base setup")


    def run(self):
        print("Base Test Execution")

class LoginTest(BaseTest):

    def run(self): # overriding
        print("Login Test Execution")

class APITest(BaseTest):
    def run(self): # overriding
        print("API Test Execution")

# jiska object create hoga uska function call hoga

ob = LoginTest()
ob.run()

ob = APITest()
ob.run()