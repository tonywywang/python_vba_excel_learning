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
binary_data = pack("!lhl", 65534,2,3)
print(binary_data)
unpack("!lhl", binary_data)
# b'\x00\x00\xff\xfe\x00\x02\x00\x00\x00\x03'  < big-endian
# b'\xfe\xff\x00\x00\x02\x00\x03\x00\x00\x00'  > little-endian
# b'\x00\x00\xff\xfe\x00\x02\x00\x00\x00\x03'  < network-endidan

# An example for extract ethernet data
ethernet_data = b'\x94\x56\x8A\x6E\x77\x43\xFF\xFF\xFF\xFF\xFF\xFF\x00\x08'
dest_mac, src_mac, protocol = unpack('! 6s 6s H', ethernet_data[:14])
print(binascii.hexlify(dest_mac), binascii.hexlify(src_mac), hex(socket.htons(protocol)))
#b'94568a6e7743' b'ffffffffffff' 0x800
ip_protocol, source_ip, target_ip = struct.unpack('! 8x B B 2x 4s 4s' , data[:20]) # x means pad value no value

#Extract the IP Header Field
ip_head = pkt[0][14:34]
ip_head_unpacked = struct.unpack("!1s1s1H1H2s1B1B2s4s4s", ip_head)#Rip out all the fields in the IP

ver_head_length = binascii.hexlify(ip_head_unpacked[0])
service_field = binascii.hexlify(ip_head_unpacked[1])
total_length = str(ip_head_unpacked[2])
identification = str(ip_head_unpacked[3])
flag_frag = binascii.hexlify(ip_head_unpacked[4])
ttl = str(ip_head_unpacked[5])
protocol = str(ip_head_unpacked[6])
checkSum = binascii.hexlify(ip_head_unpacked[7])
src_ip = socket.inet_ntoa(ip_head_unpacked[8])
dst_ip = socket.inet_ntoa(ip_head_unpacked[9])

#Extract the TCP Header
tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HHII2sH2sH", tcpHeader)

dst_port = str(tcp_hdr[0])
src_port = str(tcp_hdr[1])
seq_no = str(tcp_hdr[2])
ack_no = str(tcp_hdr[3])
head_length_6_point = binascii.hexlify(tcp_hdr[4])
window_size = str(tcp_hdr[5])
checksum = binascii.hexlify(tcp_hdr[6])
urgent_pointer = str(tcp_hdr[7])  
data = pkt[0][54:]

pack('ci', b'*', 0x12131415) # c = char i = int
# b'*\x00\x00\x00\x12\x13\x14\x15'
pack('ic', 0x12131415, b'*')
# b'\x12\x13\x14\x15*'