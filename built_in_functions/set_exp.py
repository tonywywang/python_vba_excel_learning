l1 = [1, 2, 3, 2, 4, 2, 4, 5, 3]
s1 = set(l1)
print(s1)

s1 = set()
s1.add(1)
# s1.add({1, 2}) #TypeError: unhashable type: 'set'
s1.update({1, 2})
s1.add(2)
s1.add(3)
print(s1)

theSet = {1,2,3,4,5,6}

#remove 3 using discard() function
theSet.discard(3)
print(theSet)

#call discard() function again to remove 3
theSet.discard(3) #This won't raise any exception
print(theSet)

#call remove() function to remove 5
theSet.remove(5)
print(theSet)

#call remove() function to remove 5 again
theSet.remove(5) #this would raise exception
print(theSet) #this won't be printed

A = {1, 2, 3, 4} #initializing set A
B = {2, 3, 5, 7} #initializing set B

union_operation = A.union(B)

print("A union B :")
print(union_operation)    # {1, 2, 3, 4, 5, 7}

intersection_operation = A.intersection(B)

print("A intersection B :")
print(intersection_operation)   # {2, 3}