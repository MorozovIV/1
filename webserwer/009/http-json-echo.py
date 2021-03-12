# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer # python2
from http.server import BaseHTTPRequestHandler, HTTPServer  # python3


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request")

    def do_POST(self):
        '''Reads post request body'''
        self._set_headers()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        self.wfile.write("received post request:<br>{}")

    def do_PUT(self):
        self.do_POST()


host = ''
port = 8000
print('Starting server at http://localhost:8000')
HTTPServer((host, port), HandleRequests).serve_forever()


# #!/usr/bin/env python
# # Reflects the requests with dummy responses from HTTP methods GET, POST, PUT, and DELETE
# # Written by Tushar Dwivedi (2017)
#
# import json
# # from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from optparse import OptionParser
#
# class RequestHandler(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         request_path = self.path
#
#         print("\n----- Request Start ----->\n")
#         print("request_path :", request_path)
#         print("self.headers :", self.headers)
#         print("<----- Request End -----\n")
#
#         self.send_response(200)
#         self.send_header("Set-Cookie", "foo=bar")
#         self.end_headers()
#         self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode(encoding='utf_8'))
#
#     def do_POST(self):
#         request_path = self.path
#
#         # print("\n----- Request Start ----->\n")
#         print("request_path : %s", request_path)
#
#         request_headers = self.headers
#         content_length = request_headers.getheaders('content-length')
#         length = int(content_length[0]) if content_length else 0
#
#         # print("length :", length)
#
#         print("request_headers : %s" % request_headers)
#         print("content : %s" % self.rfile.read(length))
#         # print("<----- Request End -----\n")
#
#         self.send_response(200)
#         self.send_header("Set-Cookie", "foo=bar")
#         self.end_headers()
#         self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode(encoding='utf_8'))
#
#     do_PUT = do_POST
#     do_DELETE = do_GET
#
#
# def main():
#     port = 8000
#     print('Listening on localhost:%s' % port)
#     server = HTTPServer(('', port), RequestHandler)
#     server.serve_forever()
#
#
# if __name__ == "__main__":
#     parser = OptionParser()
#     parser.usage = ("Creates an http-server that will echo out any GET or POST parameters, and respond with dummy data\n"
#                     "Run:\n\n")
#     (options, args) = parser.parse_args()
#
#     main()
# #!/usr/bin/env python3
#
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from urllib.parse import urlparse
# import json
#
# class RequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         parsed_path = urlparse(self.path)
#         print("\n----- Request Start ----->\n")
#         print("request_path :", request_path)
#         print("self.headers :", self.headers)
#         print("<----- Request End -----\n")
#         self.send_response(200)
#         self.send_header("Set-Cookie", "foo=bar")
#         self.end_headers()
#         self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode(encoding='utf_8'))
#         return
#
#     def do_POST(self):
#         content_len = int(self.headers.getheader('content-length'))
#         post_body = self.rfile.read(content_len)
#         data = json.loads(post_body)
#
#         parsed_path = urlparse(self.path)
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(json.dumps({
#             'method': self.command,
#             'path': self.path,
#             'real_path': parsed_path.query,
#             'query': parsed_path.query,
#             'request_version': self.request_version,
#             'protocol_version': self.protocol_version,
#             'body': data
#         }).encode(encoding='utf_8'))
#         return
#
# if __name__ == '__main__':
#     server = HTTPServer(('localhost', 8000), RequestHandler)
#     print('Starting server at http://localhost:8000')
#     server.serve_forever()