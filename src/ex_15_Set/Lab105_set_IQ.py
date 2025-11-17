"""
find the first non-repeating charactor in string using set.

swiss-> w, i
"""

# Creating the empty set

s = set()

def first_non_repeating(string):
    # Loop through each character in the given string
    for char in string:

        # Check if the character appears exactly once in the string
        if string.count(char) == 1:
            # If yes, this is the first non-repeating character — return it
            s.add(char)
            return char

    # If no non-repeating character is found, return None
    return None


# Test the function with "swiss"
print(first_non_repeating("swiss"))  # Output: w

print(first_non_repeating("annusingha"))
print(s)


# Frozen set

fset = frozenset([1, 2, 3, 3])
print(fset)

