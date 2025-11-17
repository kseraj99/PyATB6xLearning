
name = ["Seraj", "Khan", "QA", "Safika"]



def upper_case(string):
    return string.upper()

# up = upper_case("seraj")
# print(up)

"""
using Map
"""

upper_name = list(map(upper_case, name))

print(upper_name)