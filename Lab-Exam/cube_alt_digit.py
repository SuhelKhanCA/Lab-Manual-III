# sum of cube of alternate digit

for i in range(10000, 99999):
    num = i
    sum = 0
    while(num != 0):
        rem = num % 10
        num  = num // 10
        num  = num // 10
        sum += rem**3

    if sum == i:
        print(i)
