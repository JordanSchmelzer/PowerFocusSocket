import socket

HEADER = 64
PORT = 4545
FORMAT = "ascii"
DISCONNECT_MESSAGE = "!DISCONNECT"
HOST = "10.0.0.124"
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
