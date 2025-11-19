class Calculator:

    def __init__(self,a, b):
        print("I am a default constructor")
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

val1 = float(input("Enter the first number:\n"))
val2 = float(input("Enter the second number:\n"))

object_ref = Calculator(val1, val2)

sum_out = object_ref.sum()
sub_out = object_ref.sub()
mul_out = object_ref.mul()
div_out = object_ref.div()

print(f"sum is {sum_out},subtraction is {sub_out}, multiplication is {mul_out} and division is {div_out}")


# print(
#     f"sum is {sum_out}, "
#     f"subtraction is {sub_out}, "
#     f"multiplication is {mul_out} and "
#     f"division is {div_out}"
# )

# print(f"""
# sum is {sum_out},
# subtraction is {sub_out},
# multiplication is {mul_out},
# division is {div_out}
# """)
