
def can_you_drink(age):
    if age < 18:
        raise Exception("You are not allowed to drink")

# print(can_you_drink(17))
print(can_you_drink(25))