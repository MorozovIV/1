import os
import socket

unix_sock_name = 'unix_sock'
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
socket.AF
if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

sock.bind(unix_sock_name)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message', result.decode('utf-8'))