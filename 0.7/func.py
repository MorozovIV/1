# -*- coding: utf-8 -*-
# список функций
vers = '0.1'
server_list = ["10.10.21.1", "10.10.21.2", "10.10.21.3", "10.10.21.4", "10.10.21.5", "10.10.21.6", "10.10.21.7", "10.10.21.8", "10.10.21.9"]
list_ip = []
list_down = []

def vremya():
    import time
    vremya = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
    print('timenow: '+vremya)

def version(version):
    import socket

    hostname = socket.gethostname()  # получаем хост локальной машины
    port = 12345  # устанавливаем порт сервера
    client = socket.socket()  # создаем сокет клиента
    client.connect((hostname, port))  # подключаемся к серверу
    data = vers
    client.send(data.encode())  # отправляем сообщение серверу
    data = client.recv(1024)  # получаем данные с сервера
    print("version is actual: ", data.decode())
    client.close()  # закрываем подключение

def message(mes):
    import socket

    hostname = socket.gethostname()  # получаем хост локальной машины
    port = 12345  # устанавливаем порт сервера
    client = socket.socket()  # создаем сокет клиента
    client.connect((hostname, port))  # подключаемся к серверу
    client.send(mes.encode())  # отправляем сообщение серверу
    data = client.recv(1024)  # получаем данные с сервера
    print("Server sent: ", data.decode())
    client.close()# закрываем подключение

def serv():
    import os
    hostname = "10.10.21.1"  # example
    response = os.system("@echo ping -n 1 " + hostname)
    # and then check the response...
    if response == 0:
        print(f"{hostname} is up!")
    else:
        print(f"{hostname} is down!")

def serv_list():
    import os
    i = 0
    while i < len(server_list):
        hostname = server_list[i]
        response = os.system("@echo ping -n 1 " + hostname)
           # and then check the response...
        if response == 0:
            list_ip.append(hostname)
            # list_up.append(f"{hostname} is up!")
        else:
            list_down.append(hostname)
            # list_down.append(f"{hostname} is down!")
        i += 1
    print('хосты в сети:')
    print(list_ip)
    print('хосты не в сети:')
    print(list_down)

