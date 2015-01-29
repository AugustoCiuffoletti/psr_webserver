#!/usr/bin/python
import SimpleHTTPServer
import SocketServer

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 80), Handler)
print "Server pronto..."
httpd.serve_forever()
