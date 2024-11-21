# File handling concepts
file  = open("file.txt", "r+")

my_string = file.read()

dict1 = {v:0 for v in my_string}

for char in my_string:
    if char in dict1.keys():
        dict1[char]  = dict1[char] + 1

key  = ""
value  = -1

for i in dict1:
    if dict1[i] > value:
        value = dict1[i]
        key = i

print(key, value)
