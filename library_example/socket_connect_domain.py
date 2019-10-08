import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("socket created successfully")
except socket.error as err:
	print("Failed to create socket")

port = 80

try:
	ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
	print("There was an error in dns lookup")
	sys.exit()

try:
    s.connect((ip, port))
except socket.gaierror as e:
	print("Address related error %s" % e)
	sys.exit()

fd = s.makefile('rw', 0)
try:
	fd.write("Hello World HTTP/1.0\r\n\r\n")
except socket.error as e:
	print("Error sending data")
	sys.exit()
print("connect to www.google.com successfully on %s" %ip)
