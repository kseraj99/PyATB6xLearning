
class MathOperation:


    def div(self, a, b):
        return a/b
    # for static method you do not need to create an object reference.
    @staticmethod
    def sum(a, b):
        return a+b


t = MathOperation()
s= t.div(5,2)
print(s)

print(MathOperation.sum(4,3))