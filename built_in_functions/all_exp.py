list1 = [1,2,3,4,5]
print(all(list1)) # return true if all elements in iterable object are true
list2 = [0,1,2,3,4,5]
print(all(list2)) # return false if any element is 0 (False) 
list3 = [1,-2,3,4,-5]
print(all(list3))

print(all([]))    # null list return True
print(all(()))    # null tuple return True
print(all({}))    # null dictionary return True

print(all([{}]))  # if the element is a NULL tuple/list/dict, return False
print(all([0, 0.0, '', (), [], {}]))
if not []:
    print(False)  # Null list return False
else:
    print(True)