import socket
import logging
import time
from utils.leftpad import leftpad
from utils.screen_clear import screen_clear
from mids.mids import *

print("[CLIENT] Starting... Open Protocol Pset Extract")
msg_handler = AppMessageCodex()


HEADER = 64
PORT = 4545
FORMAT = "ascii"
DISCONNECT_MESSAGE = msg_handler.MID3()
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


# main program
client.sendall(MID1().encode(FORMAT))  # communication start
response = client.recv(1024).decode(FORMAT)
response_MID = response[4:8]
time.sleep(1)

if response_MID == "0002":
    print("[CLIENT]: I'm connected to the controller!")
    connection = True

while connection:
    print("Enter message: (quit to exit)")
    user_input = input()
    if user_input == "quit":
        connection = False

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
# screen_clear()
