
class BaseTest:

    def run(self):
        print("Running the generic Test")


class LoginTest(BaseTest):

    def run(self):
        print("Running login Test")

obj = LoginTest()
obj.run()