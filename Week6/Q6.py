# count uppercase, lowercase, alpha

my_str = input("Enter a string : ")

u_c = 0
l_c = 0
al_c = 0
dig_c = 0

for ch in my_str:
      if ch.isupper():
            u_c += 1
            al_c += 1
      if ch.islower():
            l_c += 1
            al_c += 1
      if ch.isdigit():
            dig_c += 1

print("No of uppercase : ", u_c)                              
print("No of lowercase : ", l_c)                              
print("No of aplphabets : ", al_c)                              
print("No of digits : ", dig_c)                              
            