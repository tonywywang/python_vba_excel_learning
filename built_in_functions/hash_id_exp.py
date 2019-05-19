print(hash(-1))
print(hash(-2))
print(hash(-1) == hash(-2))

print(id(-1))
print(id(-2))
print(id(-1) == id(-2))

# obj1 is obj2  means to compare their id value
# == compares the objs' value
# if an obj has a hash value, it means it can be used
# as dictionary key