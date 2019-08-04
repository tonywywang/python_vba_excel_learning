from array import *

a1 = array('d', [1.0, 2.3, 3.14]) # class array.array(typecode[, initializer])
print(a1.typecode) # d (typecode 'd' double type)
print(a1.itemsize) # 8 The length in bytes of one array item in the internal representation.
a1.append(-4.59) # like list to append value
print(a1) # array('d', [1.0, 2.3, 3.14, -4.59])
# This is only supported for values which are 1, 2, 4, or 8 bytes in size; 
# for other types of values, RuntimeError is raised. It is useful when reading
# data from a file written on a machine with a different byte order.
a1.byteswap() 
print(a1) # array('d', [3.03865e-319, 1.9035985662475526e+185, 7.9824696849641e-157, 7.387368604390227e+137])

a2 = array('B', [])
# the test.txt should be edited in hex mode
with open("test.txt", 'rb') as f:  # the file must be read from 'b' mode
    a2.fromfile(f, 4)
print(a2)
# array('B', [1, 2, 3, 4])