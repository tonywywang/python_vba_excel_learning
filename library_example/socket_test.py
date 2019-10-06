import socket
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    try:
        s.sendall(b'Hello, world')
    except socket.error as e:
        print("sendall error: %s" % e)
        sys.exit(1)

    try:
        data = s.recv(1024)
    except socket.error as e:
    	print("recv error: %s" % e)
    	sys.exit(1)

print('Received', repr(data))