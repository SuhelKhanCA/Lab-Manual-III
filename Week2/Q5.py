# Sum of digits of a number
num = int(input("Enter a number: "))
num1 = num
sum = 0
while num1 != 0:
    r = num1 % 10
    num1 //= 10 # use integer division
    sum += r

print("Sum of digits of", num, "is: ", sum)

