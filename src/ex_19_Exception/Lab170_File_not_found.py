"""
What is the difference between error and exception?

- Errors = serious issues (memory, syntax)
- Exceptions = runtime issues you can handle (Error in the end)

"""
try:
    data = open("test.json").read()
except FileNotFoundError as f:
    print(f)