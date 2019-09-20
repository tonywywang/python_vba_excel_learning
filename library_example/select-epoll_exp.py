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
                    print('-'*40 + '\n' + requests[fileno].decode()[:-2])
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
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
Line 1: The select module contains the epoll functionality.
Line 13: Since sockets are blocking by default, this is necessary to use non-blocking (asynchronous) mode.
Line 15: Create an epoll object.
Line 16: Register interest in read events on the server socket. A read event will occur any time the server socket accepts a socket connection.
Line 19: The connection dictionary maps file descriptors (integers) to their corresponding network connection objects.
Line 21: Query the epoll object to find out if any events of interest may have occurred. The parameter "1" signifies that we are willing to wait up to one second for such an event to occur. If any events of interest occurred prior to this query, the query will return immediately with a list of those events.
Line 22: Events are returned as a sequence of (fileno, event code) tuples. fileno is a synonym for file descriptor and is always an integer.
Line 23: If a read event occurred on the socket server, then a new socket connection may have been created.
Line 25: Set new socket to non-blocking mode.
Line 26: Register interest in read (EPOLLIN) events for the new socket.
Line 31: If a read event occurred then read new data sent from the client.
Line 33: Once the complete request has been received, then unregister interest in read events and register interest in write (EPOLLOUT) events. Write events will occur when it is possible to send response data back to the client.
Line 34: Print the complete request, demonstrating that although communication with clients is interleaved this data can be assembled and processed as a whole message.
Line 35: If a write event occurred on a client socket, it's able to accept new data to send to the client.
Lines 36-38: Send the response data a bit at a time until the complete response has been delivered to the operating system for transmission.
Line 39: Once the complete response has been sent, disable interest in further read or write events.
Line 40: A socket shutdown is optional if a connection is closed explicitly. This example program uses it in order to cause the client to shutdown first. The shutdown call informs the client socket that no more data should be sent or received and will cause a well-behaved client to close the socket connection from it's end.
Line 41: The HUP (hang-up) event indicates that the client socket has been disconnected (i.e. closed), so this end is closed as well. There is no need to register interest in HUP events. They are always indicated on sockets that are registered with the epoll object.
Line 42: Unregister interest in this socket connection.
Line 43: Close the socket connection.
Lines 18-45: The try-catch block is included because the example program will most likely be interrupted by a KeyboardInterrupt exception
Lines 46-48: Open socket connections don't need to be closed since Python will close them when the program terminates. They're included as a matter of good form.
'''