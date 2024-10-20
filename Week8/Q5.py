s = input("Enter A string: ")
l1 = []
l2 = []
for c in s:
    if c != " ":
        if c.isdigit():
            l2.append(c)
        else:
            l1.append(c)
print("The Number List: ", l2)
print("The Alphabet List: ", l1)