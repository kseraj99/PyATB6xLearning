"""
Write a program to Count vowels and consonants in a String.
"""

# Take input string from the user
input_str = input("Enter a string:\n")

# List of vowels (both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Counters for vowel and consonant
v_count = 0
c_count = 0

# Loop through each character in the input string
for char in input_str:

    # Check if the character is an alphabet letter (ignore numbers, space, symbols)
    if char.isalpha():

        # If the character is in the vowel list
        if char in vowels:
            v_count += 1  # Increase vowel count

        # Otherwise it's a consonant
        else:
            c_count += 1  # Increase consonant count

# Print total number of vowels
print(f"Vowels: {v_count}")

# Print total number of consonants
print(f"Consonant: {c_count}")


