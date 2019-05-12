list1 = [1,0,0,0,0]
print(any(list1)) #return true if any element in iterable object is true
list2 = []
print(any(list2))
list3 = [0,0,0]
print(any(list3))
list4 = [1,-2,3,4,-5]
print(any(list4))
print(any([]))    # null list return False
print(any(()))    # null tuple return False
print(any({}))    # null dictionary return False

print(any([{}]))  # if the element is a NULL tuple/list/dict, return False
print(any([0, 0.0, '', (), [], {}]))