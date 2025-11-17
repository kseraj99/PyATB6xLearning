"""
2️⃣ zip(key, value)
zip() combines both lists position by position.

It creates pairs like this:
("name", "Seraj")
("role", "SDET")
("experience", 3)

So zip() gives key–value pairs.

3️⃣ dict(zip(key, value))
The dict() function converts these key–value pairs into a dictionary.

"""
key = ["name", "role", "experience"]
value = ["Seraj", "SDET", 3]

my_dict = dict(zip(key,value))

print(my_dict)