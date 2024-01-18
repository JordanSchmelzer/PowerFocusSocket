import socket
import logging
import time
import os
from sys import platform

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


def send(message):
    # TODO: modify this to work with Open Protocol, this just example to work w/ server
    msg = message.encode(FORMAT)
    # msg_len = len(msg)
    # send_len = str(msg_len).encode(FORMAT)
    # send_len += b" " * (HEADER - len(send_len))
    # client.send(send_len)
    client.send(msg)
    print(client.recv(1024).decode(FORMAT))


def leftpad(str: str, final_size: int, fill_char: str):
    if str.__len__ > final_size:
        logging.fatal(
            f"[FATAL] input {str} length is larger than final size {final_size}"
        )
        return

    padded_string = fill_char * (final_size - str.__len__) + str
    return padded_string


def integrator_msg(mid, rev, data=""):
    mid_str = leftpad(mid, 4, "0")
    rev_str = leftpad(rev, 3, "0")
    ackflag_str = " "
    stationId_str = " " * 2
    spindleId_str = " " * 2
    spare_bytes = " " * 4
    header = (
        mid_str + rev_str + ackflag_str + stationId_str + spindleId_str + spare_bytes
    )

    if not data:
        return "0020" + header + chr(0)

    # TODO: build something for handling data and total str length
    return header + leftpad(data, 3, 0) + chr(0)


def screen_clear():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system("clear")
    elif platform == "darwin":
        # OSX
        os.system("clear")
    elif platform == "win32":
        # windows
        os.system("cls")
    else:  # OS niet herkend!
        print("Operating System not regconized!")


# communication start
def MID1():
    return "00200001003         " + chr(0)


# communication stop
def MID3():
    return "00200003            " + chr(0)


# get pset
def MID12(pset: int):
    return "00230012            " + leftpad(str(pset), 3, "0") + chr(0)


# pset request response
def MID0013():
    return "hello world"


# main program
send("Hello Powerfocus!" + chr(0))

client.sendall(MID1().encode(FORMAT))
response = client.recv(1024).decode(FORMAT)
response_MID = response[4:8]
time.sleep(0.5)

if response_MID == "0002":
    print("[CLIENT]: I'm connected to the controller!")
    connection = True

while connection:
    print("Enter message: (quit to exit)")
    user_input = input()
    if user_input == "quit":
        connection = False
        send(MID3())
        # screen_clear()

    if user_input:
        send(user_input)
        response = client.recv(1024).decode(FORMAT)
        logging.info(f"[SERVER] response: {response}")
        time.sleep(1)

    if response_MID == "0002":
        logging.info(
            f"[SERVER]:[" + response_MID + "]: Communication start acknowledge"
        )

    if response_MID == "0004":
        logging.info(f"[SERVER]:[" + response_MID + "]: Command error")

    if response_MID == "0005":
        logging.info(f"[SERVER]:[" + response_MID + "]: Command accepted")

    if response_MID == "0013":
        logging.info(
            f"[SERVER]:[" + response_MID + "]: Parameter set data upload reply"
        )

send(DISCONNECT_MESSAGE)
