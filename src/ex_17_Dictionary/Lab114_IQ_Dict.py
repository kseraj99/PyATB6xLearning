"""
Can we remove the duplicate value from a dictionary.
"""
# Original dictionary with some duplicate values
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}

# Set to store values that we have already seen (set keeps only unique values)
unique_value = set()

# Dictionary to store the final result with unique values
result = {}

# Loop through each key-value pair in the dictionary
for key, value in my_dict.items():

    # Check if the value has not appeared before
    if value not in unique_value:
        # Add the key-value pair to the result dictionary
        result[key] = value

        # Mark this value as seen by adding it to the set
        unique_value.add(value)

# Print the dictionary after removing duplicate values
print(result)
