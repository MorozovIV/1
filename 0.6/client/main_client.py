import socket
def time():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53211))
    client_sock.sendall(b"time")
    data = client_sock.recv(1024)
    client_sock.close()
    print('Received', repr(data)[1:]) #[1:] - удаление первого символа b

def hello():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 53211))
    client_sock.sendall(b"Hello")
    data = client_sock.recv(1024)
    client_sock.close()
    print('Received', repr(data)[1:]) #[1:] - удаление первого символа b

time()
hello()