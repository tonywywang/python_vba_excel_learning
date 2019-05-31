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