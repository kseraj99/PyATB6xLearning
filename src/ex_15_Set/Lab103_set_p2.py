"""
Union (| or union)
Combines elements from both sets.
"""
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)

print(a.union(b))

print()


"""
Intersection
Common elements in both.

"""

print(a & b)
print(a.intersection(b))


# Difference

print(a-b)
print(b-a)

"""
Symmetric Difference
Elements in either set but not both.(common ko hata do)
"""

print(a ^ b)