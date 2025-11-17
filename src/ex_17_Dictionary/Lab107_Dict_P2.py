student_info = {
    "name" : "Seraj",
    "age" : 32,
    "age" : 31,
    "address" : "Akhta"
}

# If the key will be same then the latest key value will be taken.

print(student_info)

print(student_info["name"])
print(student_info["age"])
print(student_info["address"])
student_info["age"] = 100

print(student_info["age"])