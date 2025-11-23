
class APIBase:

    def api_auth(self):
        print("Authentication API")

class DBBase:

    def db_connect(self):
        print("Connecting to the database!")


class TestHybrid(APIBase, DBBase):

    def run(self):
        self.api_auth()
        self.db_connect()
        print("Yes")

obj = TestHybrid()

obj.run()
obj.api_auth()
obj.db_connect()