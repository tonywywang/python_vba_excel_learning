from struct import *

binary_data = pack("hhl", 1,2,3)
print(binary_data)
unpack("hhl", binary_data)
# b'\x01\x00\x02\x00\x03\x00\x00\x00'
# (1, 2, 3)