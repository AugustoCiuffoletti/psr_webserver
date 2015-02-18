#!/usr/bin/python
import SimpleHTTPServer, SocketServer
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 80), Handler)
print "Server pronto..."
httpd.serve_forever()
