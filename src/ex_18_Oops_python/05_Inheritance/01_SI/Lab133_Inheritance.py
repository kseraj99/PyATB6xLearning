"""
Inheritance:-
Inheritance lets a class (child/subclass) re-use attributes and methods of
another class (parent/base).
It promotes code re-use,organization and models real-world relationships.

"""

"""
Single inheritance-
A subclass/child inherits from one Parents/Base.

"""

class BaseTest:

    def setup(self):
        print("Base setup with browser and Environment")


class LoginTest(BaseTest):

    def run(self):
        self.setup()
        print("Running the testcase")

obj = LoginTest()
obj.run()