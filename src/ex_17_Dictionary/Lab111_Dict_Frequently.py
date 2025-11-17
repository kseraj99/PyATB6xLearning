"""
Frequency of a charactor in a string.

Write a program to count the frequency of each charactor in the given string.

"""

# Logic building formula
# I/P- string e.g- automation
# O/P- dict

# Fixed string to count characters from
string = "automation"

# Taking user input
string1 = input("Enter the user input:\n")

# Empty dictionary to store character counts
char_count = {}

# Loop through each character in the string
for char in string1:
    # Use .get() to get the current count of the character
    # If the character does not exist, .get() returns 0
    # Then we add 1 to update the count
    char_count[char] = char_count.get(char, 0) + 1

# Print the final dictionary containing character counts
print(char_count)
