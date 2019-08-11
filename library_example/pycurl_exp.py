import pycurl
import sys
#from StringIO import StringIO

with open("curl_test.txt", 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://pycurl.io/')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()

with open("curl_test.txt", 'rb') as f:
    line = f.readlines()
    for elem in line:
        print(elem)