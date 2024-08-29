# print characters from a string which are present at an even index

str1  = input("Enter a string : ")

ans = ""

for i in str1[0::2]:
      print(i, end="")