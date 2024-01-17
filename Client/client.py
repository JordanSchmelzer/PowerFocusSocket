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


def buildMidMessage(mid, revision, data):
    message_end = "NUL"

    # data
    # data field (no data for this)

    # Build header
    mid = "0001"
    revision = "003"
    noAckFlag = " " * 1
    stationId = " " * 2
    spindleId = " " * 2
    spare = " " * 4
    header = mid + revision + noAckFlag + stationId + spindleId + spare
    length = header.__len__
    header_string_length = (4 - length) * " " + str(length)
    header = header_string_length + header + message_end
    message = ""

    return message


# communication start
def MID0001():
    return "00200001003         NUL"


# communication stop
def MID0003():
    return "00200003            NUL"


# get pset
def MID0012():
    return "00230012            001NUL"


send("Hello Powerfocus!")

connection = True

while connection:
    print("Enter something to send to the server")
    user_input = input()
    if user_input == "quit":
        connection = False

        send(MID0003())

    send(user_input)


send(DISCONNECT_MESSAGE)
