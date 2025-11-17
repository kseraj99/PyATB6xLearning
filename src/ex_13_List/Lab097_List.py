my_list = ["Apple", "Orange", 5, 45.05, False, "Akash", "Rohan"]

# we can change the item in the list

my_list[0] = "Mango"

my_list[5] = "Seraj"

# Now printing the list

for item in my_list: # range() function also return a list.
    print(item)

# for printing the list

for i in range(1, 5):
    print(i)

# append()- Append an object to the end of the list.
# append can add only one object at end of the list.

my_list.append("Amit")

print(my_list)

# extend()- it will add a new list in to the existing list.


my_list.extend([1.1, "Safika"])

print(my_list)

# insert()- it will update the value of a particular index.

my_list.insert(0, "Banana")

print(my_list)

my_list.insert(0, "Mango")

print(my_list)

print(len(my_list))

# we can copy the list also

copy_list = my_list.copy()

print(copy_list)