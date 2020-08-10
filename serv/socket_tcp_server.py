import socketserver

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('Adress: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        self.request.sendall(data)

if __name__=='__main__':
    with socketserver.TCPServer(('127.0.0.1', 8888), EchoTCPHandler) as server:
        server.serve_forever()