# -*- coding: utf-8 -*-
#server_0.1
# https://andreymal.org/21
ver = '0.1'
import socket
import func

func.vremya()

server = socket.socket()  # создаем объект сокета сервера
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # устанавливаем порт сервера
server.bind((hostname, port))  # привязываем сокет сервера к хосту и порту
server.listen(5)  # начинаем прослушиваение входящих подключений

print("Server running")
while True:
    con, _ = server.accept()  # принимаем клиента
    data = con.recv(1024)  # получаем данные от клиента
    message = data.decode()  # преобразуем байты в строку
    print(f"Client sent: {message}")
    print({message})
    if {message} == {"version"}:
        message = ('version server = 0.1')
        con.send(message.encode())  # отправляем сообщение клиенту
    elif {message} == {'12'}:
        message = '14'
        print(message)
        con.send(message.encode())  # отправляем сообщение клиенту
    else:
        #message = message[::-1]  # инвертируем строку
        con.send(message.encode())  # отправляем сообщение клиенту
    print(type(message))
    con.close()  # закрываем подключение
con.close()