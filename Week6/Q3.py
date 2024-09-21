# void function problem

def fuc(num):
      
      if len(str(num)) != 4:
            print("Not a 4 digit number")
            return
      else: 
            num = int(num)
            dig4 = num % 10
            num //= 10
            dig3 = num % 10
            num //= 10
            dig2 = num % 10
            num //= 10
            dig1 = num % 10
            print(dig1)
            print(dig2)
            print(dig3)
            print(dig4)
            return (dig1*10 + dig2)**2 + (dig3*10 + dig4)**2

num1 = input("Enter a four digit number : ")

print("Required sum is : ", fuc(num1))