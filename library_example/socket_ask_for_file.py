import socket
import sys

host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, 80)) # getsockaddrarg: AF_INET address must be tuple, not str
except socket.gaierror as e:
	print("Error connecting to server %s"  % e)
	sys.exit(1)

s.sendall("filename + '\r\n'".encode()) #  a bytes-like object is required, not 'str'
while True:
    buf = s.recv(2048)
    if not len(buf):
        break
    print(buf)
