import socket

# import pickle # a way to send objects to the server that it can then use to do stuff
# pretty cool, serializes the object and sends bytes. what can you do with that?

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
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello Powerfocus!")

connection = True

while connection:
    print("Enter something to send to the server")
    user_input = input()
    if user_input == "quit":
        connection = False

    send(user_input)

send(DISCONNECT_MESSAGE)
