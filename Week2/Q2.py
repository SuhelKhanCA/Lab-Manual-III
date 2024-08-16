# counting no. of digit from a number
num = int(input("Enter a number: "))
num1 = num
count = 0
while num1 != 0:
    r = num1 % 10
    num1 //= 10 # use integer division
    count += 1

print("Total no. of digits are: ", count)
