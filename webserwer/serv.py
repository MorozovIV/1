import http.server  #https://habr.com/ru/post/472464/
import socketserver
import my_modules

my_modules.vremya()
PORT = 8080
IP = '127.0.0.1'
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    print('server start http://',IP,':',PORT,sep='')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


    def do_GET(self):
        print("GET request, path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path == "/led/on":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            rasperrypi_pinout(led_pin, True)
            self.wfile.write(b"OK")
        elif self.path == "/led/off":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            rasperrypi_pinout(led_pin, False)
            self.wfile.write(b"OK")
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))