# Return sum and subtraction

def cal_sum_sub(a=0, b=0):
      sum = a+b
      sub = a-b
      
      return sum, sub

ans = cal_sum_sub()
print(f"Sum = {ans[0]} and Subtraction = {ans[1]}")
ans1 = cal_sum_sub(5, 3)
print(f"Sum = {ans1[0]} and Subtraction = {ans1[1]}")
      