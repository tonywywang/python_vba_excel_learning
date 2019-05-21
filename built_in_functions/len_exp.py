l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(id(l1), id(l2))
len(l1) # 4
d1 = {'key1': 1, 'key2':2}
len(d1) # 2
g1 = (i for i in range(50))
len(g1) # TypeError: object of type 'generator' has no len()
t1 = (1, 2, 3)
len(t1)
len(range(10)) #10