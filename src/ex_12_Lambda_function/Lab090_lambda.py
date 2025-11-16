"""
A lambda is an anonymous function that returns some form of data.
it is used for single liner function

"""
def triple_number(num):
    return num * 3


value = triple_number(3)

print(value)

# using lambda
# In this we will use Lambda, arguments and return values

result_l_f = lambda num: num*3

print(result_l_f(3))