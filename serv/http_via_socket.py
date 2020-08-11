import socket

def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status_code, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ag.ru', 80))
sock.send(b'Test message')
content_items = [
    'GET / HTTP/1.1',
    'Host: ag.ru',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('---HTTP MESSAGE---')
print(content)
print('---END OF MESSAGE---')
sock.send(content.encode())
result = sock.recv(1024)
print(result.decode())