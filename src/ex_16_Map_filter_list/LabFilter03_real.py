
names = ["QA", "", "Automation", "", "Tester"]


def non_empty(x):
    if x!= "":
        return True
    return None


non_empty1 = list(filter(non_empty, names))
print(non_empty1)