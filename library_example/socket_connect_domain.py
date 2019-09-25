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

s.connect((ip, port))
print("connect to www.google.com successfully on %s" %ip)
