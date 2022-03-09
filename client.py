import socket

HOST = 'localhost'
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Press /q to quit...')
    while True:
        message = input('> ')
        if message == '/q':
            break
        elif message == '':
            while message == '':
                print('Please enter a message.')
                message = input('> ')

        s.sendall(bytes(message, 'utf-8'))
        reply = s.recv(1024)
        if not reply:
            break
        print(str(reply, 'utf-8'))


def attach_header(msg):
    pass