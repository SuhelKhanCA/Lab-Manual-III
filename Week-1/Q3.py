# Numbers in list divisible by 5

numbers = []

print("Enter 20 numbers: ")
for _ in range(20):
    num = int(input())
    numbers.append(num)

print("Entered numbers : ", numbers)

print("Divisible by 5: ", end=" ")
for num in numbers:
    if num % 5 == 0:
        print(num, end=" ")
