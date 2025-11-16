"""
Write a Function to Check Test Case Status
Problem:
Write a function check_status(status_code) that returns:

"PASS" if status_code = 200
"FAIL" if status_code = 400 or 500
"UNKNOWN" otherwise

Example Input & Output:

print(check_status(200))   # PASS
print(check_status(500))   # FAIL
print(check_status(302))   # UNKNOWN
"""

# Defining the function
def check_status(status_code):
    match status_code:
        case 200:
            return "✅Pass"
        case 400 | 500:
            return "❌Fail"
        case _:
            return "Unknown"
# Taking the status code from the user

status_code = int(input("Enter the status code:\n"))

# Calling the function
result = check_status(status_code)
print(result)


# using if, elif and else

"""
def check_status(status_code):
    if status_code == 200:
        return "PASS"
    elif status_code == 400 or status_code == 500:
        return "FAIL"
    else:
        return "UNKNOWN"


# Taking input from the user
status = int(input("Enter the status code:\n"))

# Calling the function
print(check_status(status))

"""