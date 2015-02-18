#!/usr/bin/python
import socket
# Creazione del socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", 80))
serverSocket.listen(5)
while True:                                               # Loop di servizio
	print 'Server pronto...'
	try:
		connectionSocket, addr = serverSocket.accept()    # Attesa della connessione
	except KeyboardInterrupt:                             # Gestione dell'interruzione
		serverSocket.close(); exit(0)
	try:
		message =  connectionSocket.recv(1024)            # Lettura e controllo request-line	
	except KeyboardInterrupt:                             # Gestione dell'interruzione
       		connectionSocket.close(); serverSocket.close(); exit(0)
	if ( len(message) == 0 ):                             # Scarto un messaggio vuoto
       		connectionSocket.close(); continue
	requestLine = message.splitlines()[0]                 # Scompongo il messaggio
	(verb,filename,version) = requestLine.split()         # Scompongo lo header
	if ( ( verb != "GET" ) or ( version != "HTTP/1.1" ) ):# Semplifichiamo: solo GET ...
		connectionSocket.close(); continue
	try:
		f = open("."+filename)                            # Apertura della risorsa richiesta
	except IOError:                                       # Errore (Response "404 not found")
		connectionSocket.send("HTTP/1.1 404 Not Found\n\n") 
		connectionSocket.send("<html><head></head><body><h1>404 NoT FoUnD</html>\n")
		connectionSocket.close()
		continue
	connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")      # Invio header response "OK"
	connectionSocket.send(f.read())                       # ...seguita dall'entity con la risorsa...
	connectionSocket.send("\n")                           # ...poi chiudo il messaggio...
	connectionSocket.close()                              # ...e la connessione
    # fine del servizio!
