# Extracting each digit from a number
num = int(input("Enter a number: "))
num1 = num
rev = 0
while num1 != 0:
    r = num1 % 10
    num1 //= 10 # use integer division
    print(r, end=" ")

