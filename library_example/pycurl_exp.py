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

import certifi
PY3 = sys.version_info[0] > 2


class Test:
    def __init__(self):
        self.contents = ''
        if PY3:
            self.contents = self.contents.encode('ascii')

    def body_callback(self, buf):
        self.contents = self.contents + buf


sys.stderr.write("Testing %s\n" % pycurl.version)

t = Test()
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, 'https://curl.haxx.se/dev/')
c.setopt(c.WRITEFUNCTION, t.body_callback)
c.perform()
c.close()

print(t.contents)

import pycurl
import certifi
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

with open("curl_post_resp.txt", 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://httpbin.org/post')

    post_data = {'field': 'value'}
    # Form data must be provided already urlencoded.
    postfields = urlencode(post_data)
    # Sets request method to POST,
    # Content-Type header to application/x-www-form-urlencoded
    # and data to send in request body.
    c.setopt(c.POSTFIELDS, postfields)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
'''
POST response:
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "field": "value"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "PycURL/7.43.0.3 libcurl/7.64.1 OpenSSL/1.1.1c zlib/1.2.11 c-ares/1.15.0 libssh2/1.8.2"
  }, 
  "json": null, 
  "origin": "198.52.175.143, 198.52.175.143", 
  "url": "https://httpbin.org/post"
}
'''

# upload file with http post
import pycurl
import certifi

c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, 'https://httpbin.org/post')

c.setopt(c.HTTPPOST, [
    ('fileupload', (
        # upload the contents of this file
        c.FORM_FILE, "curl_post_resp.txt",
    )),
])

c.perform()
c.close()

import pycurl
import certifi

c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, 'https://httpbin.org/post')

c.setopt(c.HTTPPOST, [
    ('fileupload', (
        c.FORM_BUFFER, 'readme.txt',
        c.FORM_BUFFERPTR, 'This is a fancy readme file',
    )),
])

c.perform()
c.close()
'''
{
  "args": {},
  "data": "",
  "files": {
    "fileupload": "This is a fancy readme file"
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Content-Length": "221",
    "Content-Type": "multipart/form-data; boundary=------------------------bfb90951cb95a414",
    "Host": "httpbin.org",
    "User-Agent": "PycURL/7.43.0.3 libcurl/7.64.1 OpenSSL/1.1.1c zlib/1.2.11 c-ares/1.15.0 libssh2/1.8.2"
  },
  "json": null,
  "origin": "198.52.175.143, 198.52.175.143",
  "url": "https://httpbin.org/post"
}
'''

import pycurl

## Callback function invoked when download/upload has progress
def progress(download_t, download_d, upload_t, upload_d):
    print("Total to download", download_t)
    print("Total downloaded", download_d)
    print("Total to upload", upload_t)
    print("Total uploaded", upload_d)

c = pycurl.Curl()
c.setopt(c.URL, "http://slashdot.org/")
c.setopt(c.NOPROGRESS, False)
c.setopt(c.XFERINFOFUNCTION, progress)
c.perform()

import pycurl
import certifi
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, 'https://httpbin.org/put')

c.setopt(c.UPLOAD, 1)
data = '{"json":true}'
# READDATA requires an IO-like object; a string is not accepted
# encode() is necessary for Python 3
buffer = BytesIO(data.encode('utf-8'))
c.setopt(c.READDATA, buffer)

c.perform()
c.close()

'''
upload output:
{
  "args": {},
  "data": "{\"json\":true}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Content-Length": "13",
    "Host": "httpbin.org",
    "User-Agent": "PycURL/7.43.0.3 libcurl/7.64.1 OpenSSL/1.1.1c zlib/1.2.11 c-ares/1.15.0 libssh2/1.8.2"
  },
  "json": {
    "json": true
  },
  "origin": "198.52.175.143, 198.52.175.143",
  "url": "https://httpbin.org/put"
}
'''

import pycurl

## Callback function invoked when body data is ready
def body(buf):
    # Print body data to stdout
    import sys
    sys.stdout.write(buf)
    # Returning None implies that all bytes were written

## Callback function invoked when header data is ready
def header(buf):
    # Print header data to stderr
    import sys
    sys.stderr.write(buf)
    # Returning None implies that all bytes were written

c = pycurl.Curl()
c.setopt(pycurl.URL, "http://www.python.org/")
c.setopt(pycurl.WRITEFUNCTION, body)
c.setopt(pycurl.HEADERFUNCTION, header)
c.perform()

import pycurl
import sys

c1 = pycurl.Curl()
c1.setopt(pycurl.URL, "https://curl.haxx.se")
c2 = pycurl.Curl()
c2.setopt(pycurl.URL, "https://www.microsoft.com")
m = pycurl.CurlMulti()
m.add_handle(c1)
m.add_handle(c2)
while 1:
    ret, num_handles = m.perform()
    if ret != pycurl.E_CALL_MULTI_PERFORM: break
while num_handles:
    ret = m.select(1.0)
    if ret == -1:  continue   # if ret == -1 true meaning select timeout
    while 1:
        ret, num_handles = m.perform()
        if ret != pycurl.E_CALL_MULTI_PERFORM: break

import pycurl
import certifi
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.URL, "https://example.com")
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(pycurl.WRITEDATA, buffer)
c.perform()
c.close()
print(buffer.getvalue())
'''
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 50px;
        background-color: #fff;
        border-radius: 1em;
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        body {
            background-color: #fff;
        }
        div {
            width: auto;
            margin: 0 auto;
            border-radius: 0;
            padding: 1em;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is established to be used for illustrative examples in documents. You may use this
    domain in examples without prior coordination or asking for permission.</p>
    <p><a href="http://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
'''

import pycurl,urllib
from io import BytesIO
 
url = 'http://www.baidu.com'
 
headers = [
    "User-Agent:Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3",
]
 
data = {
    "cityListName":"",
    "trade": ""
}
 
c = pycurl.Curl()  #通过curl方法构造一个对象
#c.setopt(pycurl.REFERER, 'http://www.baidu.com/') #设置referer
c.setopt(pycurl.FOLLOWLOCATION, True) #自动进行跳转抓取
c.setopt(pycurl.MAXREDIRS,5)          #设置最多跳转多少次
c.setopt(pycurl.CONNECTTIMEOUT, 60)   #设置链接超时
c.setopt(pycurl.TIMEOUT,120)          #下载超时
c.setopt(pycurl.ENCODING, 'gzip,deflate') #处理gzip内容
# c.setopt(c.PROXY,ip) # 代理
c.fp = BytesIO()
c.setopt(pycurl.URL, url)   #设置要访问的URL
c.setopt(pycurl.HTTPHEADER,headers)   #传入请求头
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, urllib.parse.urlencode(data)) #传入POST数据
c.setopt(c.WRITEFUNCTION, c.fp.write) #回调写入字符串缓存
c.perform()
 
code = c.getinfo(c.HTTP_CODE) #返回状态码
html = c.fp.getvalue() #返回源代码

print(code)
print(html)
print(c.getinfo(c.TOTAL_TIME))