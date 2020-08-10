import socketserver

class EchoUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data, socket = self.request
        print('Adress: {}'.format(self.client_address[0]))
        print('Data: {}'.format(data.decode()))
        socket.sendto(data, self.client_address)

if __name__=='__main__':
    with socketserver.UDPServer(('127.0.0.1', 8888), EchoUDPHandler) as server:
        server.serve_forever()