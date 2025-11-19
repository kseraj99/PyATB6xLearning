# 1. Get input from the user
try:
    number = int(input("Enter an integer:\n"))

    # 2. Check the condition
    # The modulo operator (%) returns the remainder of a division.
    # If a number is divisible by 2, the remainder will be 0 (Even).
    # Otherwise, the remainder will be 1 (Odd).
    if number % 2 == 0:
        print(f"The number {number} is **Even**.")
    else:
        print(f"The number {number} is **Odd**.")

# Handle cases where the user enters non-integer input
except ValueError:
    print("Invalid input. Please enter a valid integer.")