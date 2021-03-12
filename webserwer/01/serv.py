#windows-----------------------------------------------------

#from threading import *
#from time import sleep

from http.server import HTTPServer, CGIHTTPRequestHandler
server_adress = ("",8000)
httpd = HTTPServer(server_adress, CGIHTTPRequestHandler)
httpd.serve_forever()
#windows-----------------------------------------------------

#linux*******************************************************
#python3 -m http.server --cgi
#linux*******************************************************

#http://localhost:8000/cgi-bin/my.py