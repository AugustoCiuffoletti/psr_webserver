#!/usr/bin/python
import socket    

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", 6789))
serverSocket.listen(1)

while True:
	print 'Server pronto...'
	try:
		connectionSocket, addr = serverSocket.accept()
	except KeyboardInterrupt:
		serverSocket.close()
		exit(0)
	try:
# Lettura e controllo request-line
		message =  connectionSocket.recv(1024)	
	except KeyboardInterrupt:
       		connectionSocket.close()
		serverSocket.close()
		exit(0)
	if ( len(message) == 0 ):
       		connectionSocket.close()
       		continue
	requestLine = message.splitlines()[0]
	(verb,filename,version) = requestLine.split()
	if ( ( verb != "GET" ) or ( version != "HTTP/1.1" ) ):
		connectionSocket.close()
		continue
# Solo Simple Request, senza Entity...
	try:
		f = open("."+filename)
	except IOError:
# File not found
		connectionSocket.send("HTTP/1.1 404 Not Found\n\n")
# Entity
		connectionSocket.send("<html><head></head><body><h1>404 Not Found</html>\n")
		connectionSocket.close()
		continue
	connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
# Invio del contenuto come entity
	connectionSocket.send(f.read())
	connectionSocket.send("\n")
	connectionSocket.close()
