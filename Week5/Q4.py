# List problem

list = [] # new list

list1 = [11, 22, 33, 45, 65, 78, 99, 101] # list 1

list2 = [11001, 2021, 330, 450, 655, 7658, 909, 205] # list 2



for i in list1:
    if i % 2 !=0:
        list.append(i)
for i in list2:
    if i % 2==0:
        list.append(i)            

print("New List is : ",list)