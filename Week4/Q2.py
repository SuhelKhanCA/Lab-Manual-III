# To check if the last element of lists are same or not
def is_same(list1, list2):
      if list1[len(list1) - 1] == list2[len(list2) - 1]:
            return True
      else:
            return False
      

print("Is same", is_same([1, 2, 3], [5, 4, 3]))
print("Is same", is_same([1, 2, 3], [5, 4, 12]))