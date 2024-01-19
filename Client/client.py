"""

"""

import logging, time, socket
from utils.leftpad import leftpad
from utils.screen_clear import screen_clear
from mids.mids import *
from utils.append_data import *


def send(message):
    # TODO: modify this to work with Open Protocol, this just example to work w/ server
    msg = message.encode(FORMAT)
    client.send(message)
    resp = client.recv(1024).decode(FORMAT)
    print(resp)


# Initialization
print("[CLIENT] Starting... Open Protocol Pset Extract")
msg_handler = AppMessageCodex()

FORMAT = "ascii"
DISCONNECT_MESSAGE = msg_handler.MID3()

print("Enter IP Address to connect to:")
host = "10.0.0.124"
port = 4545
print(host + " -port" + port)

ADDR = (host, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.sendall(msg_handler.MID1().encode(FORMAT))  # communication start
response = client.recv(1024).decode(FORMAT)
response_MID = response[4:8]
time.sleep(1)

connection = False
if response_MID == "0002":
    print("[CLIENT]: I'm connected to the controller!")
    connection = True

# Main Loop
while connection:
    print("Extract Psets from controller? [Y/n]:")
    user_input = input()

    if user_input == "quit":
        connection = False

    if user_input == "help":
        print("'quit' to close app and connections to controllers")
        print(
            "'host' arg='IP address' : change the target controller by it's IP addrerss"
        )
        print(
            "'port' arg='Port Number' : set the target controller's Open Protocol port"
        )

    if connection == True:
        if user_input[:4] == "host":
            print("set host ip address")
            host = input()
            print(f"host = {host}")
            # kill existing client
            # create chagne target addr of client obj
            # send mid1 to establish connection
            # make sure connetion is good
            # continue w/ script

        if user_input[:4] == "port":
            print("set port ip address")
            port = input()
            print(f"port = {port}")
            # kill existing client
            # create chagne target addr of client obj
            # send mid1 to establish connection
            # make sure connetion is good
            # continue w/ script

        if user_input and not user_input == "help":
            pset_index_pos = 0
            while pset_index_pos <= 999:
                client.send(msg_handler.MID12(pset_index_pos))
                response = client.recv(1024).decode(FORMAT)
                logging.info(f"[SERVER] response: {response}")
                response_MID = response[4:8]

                if response_MID == "0013":
                    time.sleep(0.005)
                    append_data_to_file(msg_handler.MID13(response))

                else:
                    print(f"[ERROR]: unexpected mid {response_MID}")

                pset_index_pos += 1
            pset_index_pos = 0

            time.sleep(1)

            if response_MID == "0004":
                msg_handler.MID4(response)

            if response_MID == "0005":
                msg_handler.MID5(response)

            print(" ")

send(DISCONNECT_MESSAGE)
# screen_clear()
