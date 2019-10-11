import socket
import time
import struct
import sys

hostname = 'time.nist.gov'
port = 37

host = socket.gethostbyname(hostname)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(''.encode(encoding='utf_8', errors='strict'), (host, port))

print("Looking for replies; press ctrl+C to stop")
buf = s.recvfrom(2048)[0]

if len(buf) != 4:
    print("wrong size reply %d, %s" % (len(buf), buf))
    sys.exit(1)

secs = struct.unpack('!I', buf)[0]
secs -= 2208988800
print(time.ctime(int(secs)))