"""
If you want to raise an exception by own, we can raise the exception like this.
"""
def vwo_login(user):
    if user != "admin":
        raise Exception("Unauthorized access!")
    return "Welcome User"

# print(vwo_login("seraj"))
print(vwo_login("admin"))