
class Father1:

    def money(self):
        print("F1 Money")

class Father2:

    def money(self):
        print("F2 Money")

# Child class me jo pahle hoga wahi call hoga.(Very Important)
# class Child(Father1, Father2):
class Child(Father2,Father1):
    def give_money(self):
        print("son")
        self.money()

obj_ref = Child()

obj_ref.give_money()