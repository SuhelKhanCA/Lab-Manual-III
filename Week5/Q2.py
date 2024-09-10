# Choosing a random character from a string

import random as rd 

my_string = input("Enter a string: ")

str_len = len(my_string)

index_flt = rd.random() * str_len

index_int = int(index_flt)


print("Random string is: ", my_string[index_int])