
# num = int(input("Enter the number:\n"))
#
# for i in range(1,num+1):
#     print("*"*i)


# Ask the user how many rows the triangle should have
rows = int(input("Enter the number:\n"))

# Outer loop: i goes from 1 to rows (inclusive)
for i in range(1, rows + 1):
    # Inner loop: print i stars on the same line
    for j in range(i):
        # print a star without moving to a new line (end="")
        print("*", end="")
    # After printing i stars, print() moves to the next line
    print()
