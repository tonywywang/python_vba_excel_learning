from struct import *
from ctypes import create_string_buffer
import binascii

binary_data = pack("hhl", 1,2,3)
print(binary_data)
unpack("hhl", binary_data)
# b'\x01\x00\x02\x00\x03\x00\x00\x00'
# (1, 2, 3)
calcsize('hhl')
# 8
# h short size
# l long size

buffer = create_string_buffer(7)  
  
#开始打包  
#偏移位置0，打包格式!B，打包数据10，10按照1个字节长度打包为0x0a  
#执行后，buffer变为：0a000000000000  
pack_into('!B', buffer, 0, 10)   
#偏移位置1，打包格式!H，打包数据11，11按照2个字节长度打包为0x000b  
#执行后，buffer变为：0a000b00000000  
pack_into('!H', buffer, 1, 11)  
#偏移位置3，打包格式!I，打包数据12，12按照4个字节长度打包为0x0000000c  
#执行后，buffer变为：0a000b0000000c  
pack_into('!I', buffer, 3, 12)   
#输出结果：0a000b0000000c  
print(binascii.hexlify(buffer))
# b'0a000b0000000c'

#开始解包  
p1 = unpack_from('!B',buffer,0)  
p2 = unpack_from('!H',buffer,1)  
p3 = unpack_from('!I',buffer,3)  
print(p1,p2,p3)  
print(p1[0],p2[0],p3[0])
# (10,) (11,) (12,)
# 10 11 12

binary_data = pack(">lhl", 65534,2,3)
print(binary_data)
unpack(">lhl", binary_data)
binary_data = pack("<lhl", 65534,2,3)
print(binary_data)
unpack("<lhl", binary_data)
# b'\x00\x00\xff\xfe\x00\x02\x00\x00\x00\x03'  < big-endian
# b'\xfe\xff\x00\x00\x02\x00\x03\x00\x00\x00'  > little-endian
