
class MathClass:

    def add(self,a, b, c= 12):
        return a+b+c

# Proper method overloading is not possible in python.

obj = MathClass()
ans1 = obj.add(2,3,4)
ans2 = obj.add(3.12,4.11)

print(ans1)
print(ans2)