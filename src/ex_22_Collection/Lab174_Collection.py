"""
In python package, there are different type of module.
"""

from collections import *

# user_input = input("Enter a string:\n")
#
# count_char = Counter(user_input)
# print(count_char)

# NamedTuple



info = namedtuple("info", ["name", "age", "ismarried", "number"])
t = info("seraj", 3.4, True, 9.8)

print(t.name)
print(t.age)
print(t.ismarried)
print(t.number)


