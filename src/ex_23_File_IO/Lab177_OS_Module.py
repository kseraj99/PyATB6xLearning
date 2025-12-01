import os

full_path = os.path.join(os.getcwd(),"testdata.txt")

with open(full_path) as f:
    data = f.read()
    print(data)