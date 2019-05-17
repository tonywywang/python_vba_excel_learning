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