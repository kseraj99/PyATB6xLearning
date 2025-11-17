"""
A Set is an 'unordered' collection of data types that is iterable,
mutable and has 'no duplicate elements'.

- Collection of Unique items.
- Start with {}
- Order is different. (No order)`
- unindexed

"""

a_set = {1, 2, 3, 3, 4, 4, 5}

print(a_set)

# converting list into a set.

alist = [45.2, 33, 33, 45, 21]

my_set = set(alist)

print(my_set)

mix = {1, "QA", False, 3.5}

print(mix)

empty_set = set()

print(type(empty_set))

for item in mix:
    print(item)

mix.add(4)

print(mix)