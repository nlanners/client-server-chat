import socket
import lib

HOST = 'localhost'
PORT = 4444

# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        print('Press /q to quit...')
        while True:
            # receive message
            message = conn.recv(1024)
            if not message:
                break
            # get data about message
            recv_len, head_len, rec_header, message_start = lib.process_header(message)
            # receive all of the message
            while recv_len != head_len + rec_header['content-length'] + 2:
                message += conn.recv(1024)

            # display message
            print(str(message[message_start:], 'utf-8'))

            # prompt for message
            reply = lib.create_reply()
            if reply == '/q':
                break

            # create header
            send_header = lib.create_header(reply)
            # attach header and encode
            send_message = lib.attach_header(reply, send_header)

            # send message
            conn.sendall(send_message)



