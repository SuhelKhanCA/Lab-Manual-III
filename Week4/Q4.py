# Iterating two list simultaneously

list1 = [1, 2, 3]
list2 = [11, 22, 33, 100]

n = len(list1) + len(list2) - 1

k =0
i = 0
j= len(list2)-1
while k <= n:
      if k < len(list1):
            print(list1[i], end=" ")
            i += 1
      else:
            print(list2[j], end=" ")
            j -= 1
      k += 1
            
            