import socket

HOST = 'localhost'
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        print('Press /q to quit...')
        while True:
            message = conn.recv(1024)
            if not message:
                break
            print(str(message, 'utf-8'))
            reply = input('> ')
            if reply == '':
                while reply == '':
                    print('Please enter a message.')
                    reply = input('> ')

            if reply == '/q':
                break
            conn.sendall(bytes(reply, 'utf-8'))
