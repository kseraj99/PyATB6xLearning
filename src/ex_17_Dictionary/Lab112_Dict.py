
dict1 = {"a": 1, "b": 2, "c": 3}

print(dict1.keys())
print(dict1.values())

dict2 = {"a": 2, "b": 2}

# For API testing we are going to use to find the difference between two json.
missing_keys = set(dict1.keys()-dict2.keys())
print(missing_keys)