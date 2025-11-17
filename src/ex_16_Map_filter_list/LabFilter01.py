"""
✅filter() — Filter Elements Based on a Condition**
filter(function, iterable)`
→ Filters elements of an iterable using a condition (returns only those that match `True`).

"""

num1 = [1, 2, 3, 4, 5, 6]

def even_number(x):
    return x%2==0

# print(even_number(5))
# print(even_number(4))


new_even_numbers = list(filter(even_number, num1))
print(new_even_numbers)

