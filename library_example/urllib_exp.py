import urllib, sys
import urllib.request

host = sys.argv[1]
file = sys.argv[2]

f = urllib.request.urlopen('http://%s%s' % (host, file))
for line in f.readlines():
    sys.stdout.write(line)
