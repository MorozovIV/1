import socket
import datetime

def time_now1():
    vremya = datetime.datetime.now()
    print(vremya)

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53211))
serv_sock.listen(10)
print('сервер запущен')

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if data ==b"time":
            time_now1()
            data = time_now1()
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()