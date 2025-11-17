
test_result = ["PASS", "FAIL", "PASS", "SKIP", "FAIL"]

pass_give = list(filter(lambda x:x=="PASS", test_result ))

print(pass_give)


list_student = [50, 100, 75]

def keep_student(x):
    return x>50



# print(keep_student(49))
# print(keep_student(80))

student = list(filter(keep_student, list_student))
print(student)