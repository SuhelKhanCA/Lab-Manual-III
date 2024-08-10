# Cube of all numbers from 1 to given number

num = int(input("Enter a number: "))

print("Cube of numbers from 1 to ", num, " are: ", end=" ")
for number in range(1, num + 1):
    print((number ** 3), end=" ")