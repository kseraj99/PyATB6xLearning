"""
Write a program to find the vowel from the string.(a,e,i,o,u)
"""

# Input string in which we want to count vowels
input_string = "Hello World!"

# Define vowels we want to check for
vowels = "aeiou"

# Variable to count how many vowels appear in the string
vowel_count = 0

# List to store the vowels found in the string
result = list()

# Loop through each character in the input string
for char in input_string:

    # Check if the character is a vowel
    if char in vowels:
        # Increase the vowel counter by 1
        vowel_count += 1

        # Add the vowel to the result list
        result.append(char)

# Print the total number of vowels
print(vowel_count)

# Print the list of vowels found in the string
print(result)

