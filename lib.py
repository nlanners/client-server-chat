import json


def create_header(msg):
    """Creates a header for msg"""
    msg_len = len(msg)
    head = {
        'content-length': msg_len,
        'content-type': 'utf-8'
    }

    return json.dumps(head).encode('utf-8')


def attach_header(msg, head):
    """Combines msg and head and encodes the full message into bytes"""
    head_len = len(head).to_bytes(2, 'big')
    return head_len + head + bytes(msg, 'utf-8')


def get_head_len(data):
    """Extract the header length from the byte data received"""
    return int.from_bytes(data[0:2], 'big')


def parse_header(msg, header_len):
    """Parse the byte msg into a dictionary (JSON) and caluclates the message start"""
    head = json.loads(msg[2:header_len+2].decode('utf-8'))
    msg_start = header_len + 2

    return head, msg_start


def create_reply():
    """Prompts for user input"""
    rply = input('> ')
    if rply == '':
        while rply == '':
            print('Please enter a message.')
            rply = input('> ')

    return rply


def process_header(data):
    """Returns information about the header"""
    # get header length
    head_len = get_head_len(data)
    # parse header and calculate message start
    rec_header, message_start = parse_header(data, head_len)
    # return number of bytes received
    return len(data), head_len, rec_header, message_start

