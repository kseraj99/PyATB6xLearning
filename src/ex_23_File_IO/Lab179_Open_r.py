
try:
    with open("testdata1.txt") as f:
        data = f.read()
        print(data)

except FileNotFoundError as fnf:
    print(fnf)