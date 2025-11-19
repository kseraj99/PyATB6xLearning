# Define a class named 'Calculator' to perform basic arithmetic operations
class Calculator:

    # The constructor method, automatically called when a new object is created
    def __init__(self):
        # Print a message indicating the constructor is executed
        print("I am a default constructor")

    # Method to calculate the sum of two numbers, 'a' and 'b'
    def sum(self, a, b):
        return a + b

    # Method to calculate the difference (subtraction) of two numbers
    def sub(self, a, b):
        return a - b

    # Method to calculate the product (multiplication) of two numbers
    def mul(self, a, b):
        return a * b

    # Method to calculate the quotient (division) of two numbers
    def div(self, a, b):
        # Note: This division will raise a ZeroDivisionError if b is 0
        return a / b

# --- Program Execution ---

# Prompt the user to enter the first number and convert the input to a float
val1 = float(input("Enter the first number:\n"))
# Prompt the user to enter the second number and convert the input to a float
val2 = float(input("Enter the second number:\n"))

# Create an object (instance) of the Calculator class.
# This automatically calls the __init__ constructor.
object_ref = Calculator()

# Call the 'sum' method on the object with inputs a and b, storing the result
sum_out = object_ref.sum(val1,val2)
# Call the 'sub' method on the object, storing the result
sub_out = object_ref.sub(val1,val2)
# Call the 'mul' method on the object, storing the result
mul_out = object_ref.mul(val1,val2)
# Call the 'div' method on the object, storing the result
div_out = object_ref.div(val1,val2)

# Print all the calculated results (sum, subtraction, multiplication, division)
print(sum_out, sub_out, mul_out, div_out)
