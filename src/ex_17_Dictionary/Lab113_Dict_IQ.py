"""
Write a program to fine the maximum value from a dictionary.
"""

aDict = {"a": 10, "b": 20, "c": 30}

def max_value_dict(dictionary):
    # return max(dictionary.values())
    return min(dictionary.values())

print(max_value_dict(aDict))
