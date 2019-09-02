import socket

ip = socket.gethostbyname('www.google.com')
print(ip)

import socket
import sys

try:
    ip = socket.gethostbyname('www.goooooooooooogle.com')
except socket.gaierror: 
  
    # this means could not resolve the host 
    print("there was an error resolving the host")
    sys.exit() 
print(ip)