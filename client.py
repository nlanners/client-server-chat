import socket

HOST = 'localhost'
PORT = 4444

message = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while message != '/q':
        message = bytes(input('Enter message: '), 'utf-8')
        s.sendall(message)
        reply = s.recv(1024)
        print(reply)
