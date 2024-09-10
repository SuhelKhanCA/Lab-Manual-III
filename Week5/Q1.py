# 6-digit OTP

import random as rd

num = rd.random() * 1000000

OTP = int(num)

print("Your OTP is: ", OTP)