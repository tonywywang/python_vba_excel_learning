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