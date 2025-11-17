from src.ex_13_List.Lab097_List import my_list

# pop()- pop will remove default last value from the list or indexing value as well.


new_list = [1, 2, 3, 1.1, "Seraj", "Pawan"]

new_list.pop()

print(new_list)

new_list.pop(3)

print(new_list)

# clear()- it will clear the list

# new_list.clear()

# print(new_list)

# count()- it will count the index value occurrence.


num = [10, 10, 20, 20, 50, 30, 40]

print(num)

print(num.count(10))

# sort()- we can sort the list as well.

num.sort()
print(num)

# reverse()- we can reverse the list as well.

num.sort(reverse=True)

print(num)

# max, min and sum is also available in the list.

print(max(num))
print(min(num))
print(sum(num))

# slicing
print(num)
print(num[1:4])

print(num[-1])

# in function is also work in the list

print(20 in num)

print("Apple" in num)

# List creation and comprehension

# range(1, 5) -> it will return the list

lis = list(range(1,5))
print(lis)
