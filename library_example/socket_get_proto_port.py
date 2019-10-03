import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = socket.getservbyname('http', 'tcp')
print("Proto port:%d" % port)
s.connect(("www.google.com", port))