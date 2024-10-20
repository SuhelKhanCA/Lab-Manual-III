lst = list(map(int, input("Enter Elements Seprated - even :").split()))
if len(lst) % 2 != 0:
    print("The list don't have even number of elements.")
else:
    lst.sort()
    mid = len(lst)//2
    lst1 = lst[:mid]
    lst2 = lst[mid:]
    print(lst1)
    print(lst2)