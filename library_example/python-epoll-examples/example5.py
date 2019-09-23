import socket, select

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(1)
serversocket.setblocking(0)

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
   connections = {}; requests = {}; responses = {}
   while True:
      events = epoll.poll(1)
      for fileno, event in events:
         if fileno == serversocket.fileno():
            connection, address = serversocket.accept()
            connection.setblocking(0)
            epoll.register(connection.fileno(), select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            responses[connection.fileno()] = response
         elif event & select.EPOLLIN:
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
               epoll.modify(fileno, select.EPOLLOUT)
               connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
               print('-'*40 + '\n' + requests[fileno].decode()[:-2])
         elif event & select.EPOLLOUT:
            byteswritten = connections[fileno].send(responses[fileno])
            responses[fileno] = responses[fileno][byteswritten:]
            if len(responses[fileno]) == 0:
               connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 0)
               epoll.modify(fileno, 0)
               connections[fileno].shutdown(socket.SHUT_RDWR)
         elif event & select.EPOLLHUP:
            epoll.unregister(fileno)
            connections[fileno].close()
            del connections[fileno]
finally:
   epoll.unregister(serversocket.fileno())
   epoll.close()
   serversocket.close()
'''
Listen Backlog Queue Size
In Examples 1-4, line 12 has shown a call to the serversocket.listen() method. 
The parameter for this method is the listen backlog queue size. It tells the 
operating system how many TCP/IP connections to accept and place on the backlog 
queue before they are accepted by the Python program. Each time the Python program 
calls accept() on the server socket, one of the connections is removed from the 
queue and that slot can be used for another incoming connection. If the queue is 
full, new incoming connections are silently ignored causing unnecessary delays 
on the client side of the network connection. A production server usually handles 
tens or hundreds of simultaneous connections, so a value of 1 will usually be 
inadequate. For example, when using ab to perform load testing against these sample 
programs with 100 concurrent HTTP 1.0 clients, any backlog value less than 50 would 
often produce performance degradation.

TCP Options
The TCP_CORK option can be used to "bottle up" messages until they are ready to send.
This option, illustrated in lines 34 and 40 of Example 5, might be a good option to 
use for an HTTP server using HTTP/1.1 pipelining.
'''