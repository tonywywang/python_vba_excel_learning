from array import *

a1 = array('d', [1.0, 2.3, 3.14]) # class array.array(typecode[, initializer])
print(a1.typecode) # d (typecode 'd' double type)
print(a1.itemsize) # 8 The length in bytes of one array item in the internal representation.