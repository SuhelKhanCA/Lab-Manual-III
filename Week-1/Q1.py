# Product of two numbers less than target
num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

while True:
    if sum < 5000:
        print("Sum is : ", sum)
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
