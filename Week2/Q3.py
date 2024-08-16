# Printing prime numbers
print("Enter a range (start, end):")

start = int(input())
end  = int(input())

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True    

for i in range(start, end+1):
    if is_prime(i):
        print(i, end=" ")

