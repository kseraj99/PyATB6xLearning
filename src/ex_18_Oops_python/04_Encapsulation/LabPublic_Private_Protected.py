
class TestExample:

    def __init__(self):
        self.driver = "Chrome"       # Public
        self._config = "Stage"       # Protected
        self.__API__key = "ABC1234"  # Private

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__API__key}")


obj_ref = TestExample()

obj_ref.show()

# Access Level

# print(obj_ref.driver)    # ✅ Public- accessible
# print(obj_ref._config)   # ⚠️ Protected- accessible, but not recommended
# print(obj_ref.__API__key)# ❌ Private- AttributeError
