"""
Triangle Classifier.

Write a program that classifies a triangle bases on its side lengths.

Given three input values representing the lengths of the sides,
determine if the triangle is equilateral (all sided are equal), isosceles
(exactly two sides are equal), scalene (no sides are equal)

"""
# Taking the triangle values from user

side1 = float(input("Enter the first side:\n"))
side2 = float(input("Enter the second side:\n"))
side3 = float(input("Enter the third side:\n"))

# Declaration of a function
def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                return "Equilateral "
            elif a == b or b == c or c == a:
                return "Isosceles"
            else:
                return "scalene"
        else:
            return "Not a triangle"
    else:
        return "Not a valid Length"


# Calling function by variable
triangle_value = classify_triangle(side1, side2, side3)

print(triangle_value)