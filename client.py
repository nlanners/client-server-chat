"""
SOURCES:
Beginning help, socket setup help: https://realpython.com/python-sockets/#echo-server
Convert bytes to int: https://www.geeksforgeeks.org/how-to-convert-bytes-to-int-in-python/
Convert dict to bytes and back: https://www.geeksforgeeks.org/python-interconversion-between-dictionary-and-bytes/
Basic Socket setup: https://docs.python.org/3.4/howto/sockets.html
"""


import socket
import lib

# global variables
HOST = 'localhost'
PORT = 4444

# create socket and connect to server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Press /q to quit...')

    while True:
        # prompt for message
        message = lib.create_reply()
        if message == '/q':
            break

        # create a header for the message
        header = lib.create_header(message)
        # link header to message and encode
        send_message = lib.attach_header(message, header)

        # send message
        s.sendall(send_message)

        # receive a reply from server
        reply = s.recv(1024)
        if not reply:
            break
        # get data about message
        recv_len, reply_head_len, reply_header, reply_start = lib.process_header(reply)
        # receive all of the message
        while recv_len != reply_head_len + reply_header['content-length'] + 2:
            reply += s.recv(1024)
        # display message
        print(str(reply[reply_start:], 'utf-8'))






