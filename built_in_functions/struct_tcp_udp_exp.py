import socket
import struct

'''
struct format:
Character	Byte order	    Size	   Alignment
@	        native	        native	   native
=	        native	        standard   none
<	        little-endian	standard   none
>	        big-endian	    standard   none
!	 network (= big-endian)	standard   none

Format	C Type	        Python type	       Standard size	  Notes
x	    pad byte	    no value	 	 
c	    char	        string of length 1	   1	 
b	    signed char	    integer	               1	          (3)
B	    unsigned char   integer	               1 	          (3)
?	    _Bool	        bool	               1	          (1)
h	    short	        integer	               2	          (3)
H	    unsigned short	integer	               2	          (3)
i	    int	            integer	               4	          (3)
I	    unsigned int	integer	               4	          (3)
l	    long	        integer	               4	          (3)
L	    unsigned long	integer	               4	          (3)
q	    long long	    integer	               8	          (2), (3)
Q	 unsigned long long	integer	               8	          (2), (3)
f	    float	        float	               4	          (4)
d	    double	        float	               8	          (4)
s	    char[]	        string	 	 
p	    char[]	        string	 	 
P	    void *	        integer	 	                          (5), (3)

Notes:
(1) The '?' conversion code corresponds to the _Bool type defined by C99. 
    If this type is not available, it is simulated using a char. 
    In standard mode, it is always represented by one byte.

    New in version 2.6.

(2) The 'q' and 'Q' conversion codes are available in native mode only if 
    the platform C compiler supports C long long, or, on Windows, __int64. 
    They are always available in standard modes.

    New in version 2.2.

(3) When attempting to pack a non-integer using any of the integer conversion codes, 
    if the non-integer has a __index__() method then that method is called to convert 
    the argument to an integer before packing. If no __index__() method exists, 
    or the call to __index__() raises TypeError, then the __int__() method is tried. 
    However, the use of __int__() is deprecated, and will raise DeprecationWarning.
    Changed in version 2.7: Use of the __index__() method for non-integers is new in 2.7.
    Changed in version 2.7: Prior to version 2.7, not all integer conversion codes would 
    use the __int__() method to convert, and DeprecationWarning was raised only for float arguments.

(4) For the 'f' and 'd' conversion codes, the packed representation uses the IEEE 754 binary32 
    (for 'f') or binary64 (for 'd') format, regardless of the floating-point format used by the platform.

(5) The 'P' format character is only available for the native byte ordering (selected as the 
    default or with the '@' byte order character). The byte order character '=' chooses to 
    use little- or big-endian ordering based on the host system. The struct module does not 
    interpret this as native ordering, so the 'P' format is not available.
'''
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

class IP(object):
	def __init__(self, source, destination, payload='', proto=socket.IPPROTO_TCP):
		self.version = 4
		self.ihl = 5 # Internet Header Length
		self.tos = 0 # Type of Service
		self.tl = 20+len(payload)
		self.id = 0#random.randint(0, 65535)
		self.flags = 0 # Don't fragment
		self.offset = 0
		self.ttl = 255
		self.protocol = proto
		self.checksum = 2 # will be filled by kernel
		self.source = socket.inet_aton(source)
		self.destination = socket.inet_aton(destination)
	def pack(self):
		ver_ihl = (self.version << 4) + self.ihl
		flags_offset = (self.flags << 13) + self.offset
		ip_header = struct.pack("!BBHHHBBH4s4s",
					ver_ihl,
					self.tos,
					self.tl,
					self.id,
					flags_offset,
					self.ttl,
					self.protocol,
					self.checksum,
					self.source,
					self.destination)
		self.checksum = checksum(ip_header)
		ip_header = struct.pack("!BBHHHBBH4s4s",
					ver_ihl,
					self.tos,
					self.tl,
					self.id,
					flags_offset,
					self.ttl,
					self.protocol,
					socket.htons(self.checksum),
					self.source,
					self.destination)  
		return ip_header
	def unpack(self, packet):
		_ip = layer()
		_ip.ihl = (ord(packet[0]) & 0xf) * 4
		iph = struct.unpack("!BBHHHBBH4s4s", packet[:_ip.ihl])
		_ip.ver = iph[0] >> 4
		_ip.tos = iph[1]
		_ip.length = iph[2]
		_ip.ids = iph[3]
		_ip.flags = iph[4] >> 13
		_ip.offset = iph[4] & 0x1FFF
		_ip.ttl = iph[5]
		_ip.protocol = iph[6]
		_ip.checksum = hex(iph[7])
		_ip.src = socket.inet_ntoa(iph[8])
		_ip.dst = socket.inet_ntoa(iph[9])
		_ip.list = [
			_ip.ihl,
			_ip.ver,
			_ip.tos,
			_ip.length,
			_ip.ids,
			_ip.flags,
			_ip.offset,
			_ip.ttl,
			_ip.protocol,
			_ip.src,
			_ip.dst]
		return _ip

class TCP(object):
	def __init__(self, srcp, dstp):
		self.srcp = srcp
		self.dstp = dstp
		self.seqn = 10
		self.ackn = 0
		self.offset = 5 # Data offset: 5x4 = 20 bytes
		self.reserved = 0
		self.urg = 0
		self.ack = 0
		self.psh = 0
		self.rst = 0
		self.syn = 1
		self.fin = 0
		self.window = socket.htons(5840)
		self.checksum = 0
		self.urgp = 0
		self.payload = ""
	def pack(self, source, destination):
		data_offset = (self.offset << 4) + 0
		flags = self.fin + (self.syn << 1) + (self.rst << 2) + (self.psh << 3) + (self.ack << 4) + (self.urg << 5)
		tcp_header = struct.pack('!HHLLBBHHH', 
					 self.srcp, 
					 self.dstp, 
					 self.seqn, 
					 self.ackn, 
					 data_offset, 
					 flags,  
					 self.window,
					 self.checksum,
					 self.urgp)
		#pseudo header fields
		source_ip = source
		destination_ip = destination
		reserved = 0
		protocol = socket.IPPROTO_TCP
		total_length = len(tcp_header) + len(self.payload)
		# Pseudo header
		psh = struct.pack("!4s4sBBH",
			  source_ip,
			  destination_ip,
			  reserved,
			  protocol,
			  total_length)
		psh = psh + tcp_header + self.payload
		tcp_checksum = checksum(psh)
		tcp_header = struct.pack("!HHLLBBH",
				  self.srcp,
				  self.dstp,
				  self.seqn,
				  self.ackn,
				  data_offset,
				  flags,
				  self.window)
		tcp_header+= struct.pack('H', tcp_checksum) + struct.pack('!H', self.urgp)
		return tcp_header
	def unpack(self, packet):
		cflags = { # Control flags
			32:"U",
			16:"A",
			8:"P",
			4:"R",
			2:"S",
			1:"F"}
		_tcp = layer()
		_tcp.thl = (ord(packet[12])>>4) * 4
		_tcp.options = packet[20:_tcp.thl]
		_tcp.payload = packet[_tcp.thl:]
		tcph = struct.unpack("!HHLLBBHHH", packet[:20])
		_tcp.srcp = tcph[0] # source port
		_tcp.dstp = tcph[1] # destination port
		_tcp.seq = tcph[2] # sequence number
		_tcp.ack = hex(tcph[3]) # acknowledgment number
		_tcp.flags = ""
		for f in cflags:
			if tcph[5] & f:
				_tcp.flags+=cflags[f]
		_tcp.window = tcph[6] # window
		_tcp.checksum = hex(tcph[7]) # checksum
		_tcp.urg = tcph[8] # urgent pointer
		_tcp.list = [
			_tcp.srcp,
			_tcp.dstp,
			_tcp.seq,
			_tcp.ack,
			_tcp.thl,
			_tcp.flags,
			_tcp.window,
			_tcp.checksum,
			_tcp.urg,
			_tcp.options,
			_tcp.payload]
		return _tcp

class UDP(object):
	def __init__(self, src, dst, payload=''):
		self.src = src
		self.dst = dst
		self.payload = payload
		self.checksum = 0
		self.length = 8 # UDP Header length
	def pack(self, src, dst, proto=socket.IPPROTO_UDP):
		length = self.length + len(self.payload)
		pseudo_header = struct.pack('!4s4sBBH',
			socket.inet_aton(src), socket.inet_aton(dst), 0, 
			proto, length)
		self.checksum = checksum(pseudo_header)
		packet = struct.pack('!HHHH',
			self.src, self.dst, length, 0)
		return packet