# -*- coding: utf-8 -*-
#client_0.1
import socket

hostname = socket.gethostname()  # получаем хост локальной машины
port = 12345  # устанавливаем порт сервера
client = socket.socket()  # создаем сокет клиента
client.connect((hostname, port))  # подключаемся к серверу
message = input("Input a text: ")  # вводим сообщение
client.send(message.encode())  # отправляем сообщение серверу
data = client.recv(1024)  # получаем данные с сервера
print("Server sent: ", data.decode())
client.close()# закрываем подключение
