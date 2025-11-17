"""
Dictionary
- Key and Value Pair.
- A dictionary is an unordered, mutable, and indexed collection of key-value pairs in Python.
- It is defined using curly braces {}.
- Where it will be used - API Automation( JSON -, Dict)
"""

my_dict = {
    "Name": "Seraj",
    "Age": 32,
    "Role": "SDET",
    "Experience": 3
}

print(my_dict)
print(my_dict["Age"])
print(my_dict["Role"])

my_dict["Role"] = "Manual Tester" # it is mutable in nature.
print(my_dict)

"""
If you want to loop through both keys and values, you need to use'.items()'.
"""

for key,value in my_dict.items():
    # print(key)
    # print(value)
    print(key,value)

print("Age" in my_dict)
print("Role" in my_dict)
print("Title" in my_dict)