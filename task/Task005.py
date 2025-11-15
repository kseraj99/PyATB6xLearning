"""
In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches

True - why >  Strip and convert them into the lowercase = both of them are equal.
"""

expected_title = "Dashboard"
actual_title = "Dashboard "

# Here we will use .strip() function to remove the extra space from the string

if expected_title.strip() == actual_title.strip():
    print("API Request Passed ✅")
else:
    print("API Request Failed ❌")