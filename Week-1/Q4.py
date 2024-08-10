# Given number is palindrome or not

num = int(input("Enter a number : "))

num1 = num # Kisi fxn se krne pe ye change nhi hoga extra  variable ki jarurat nhi pdegi
rev = 0
while num1 != 0:
    r = num1 % 10
    num1 //= 10 # use integer division
    rev = rev * 10 + r

if num == rev:
    print(num, "- is Palindrome")
else:
    print(num, "- is not Palindrome")  
