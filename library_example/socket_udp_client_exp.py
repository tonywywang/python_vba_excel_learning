import socket
import sys

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    port = s.getservbyname(textport, 'udp')

s.connect((host, port))
print("Enter some message to send:")
message = sys.stdin.readline().strip()
s.sendall(message.encode(encoding='utf_8', errors='strict'))
print("Ctrl + C to terminate")
while 1:
	buf = s.recv(2048).decode(encoding='utf_8', errors='strict')
	if not len(buf):
		break
	sys.stdout.write(buf)