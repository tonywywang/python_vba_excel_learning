import socket
import struct

ETH_P_IP = 0x0800 # Internet Protocol Packet

class Ether:
    def __init__(self, src, dst, type=ETH_P_IP):
    	self.src = src
    	self.dst = dst
    	self.type = type
    def pack(self):
    	ethernet = struct.pack('!6s6sH',
    		self.dst,
    		self.src,
    		self.type)
    	return ethernet