# File handling concepts
file  = open("file.txt", "r+")
file1  = open("file.txt", "r+")
print(len(file.readlines())) # count number of lines
my_string = file1.read()

list = my_string.split()

print(len(list))

dict1 = {v: 0 for v in my_string}

print(len(dict1))