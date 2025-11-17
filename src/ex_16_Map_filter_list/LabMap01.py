"""
✅ MAP() and FILTER() in Python
map(function, iterable)

→ Applies a function to each item in a list (or any iterable)
and returns a map object (iterator).

"""
numbers = [1, 2, 3, 4, 5]


def sq(x):
    return x**2


# val = sq(5)
# print(val)

sq_all_numbers = list(map(sq, numbers))
print(sq_all_numbers)