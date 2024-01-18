"""
A_INET = IPv4

2 Kinds of sockets:
SOCK_STREAM -> Transmission Control Protocol (TCP)
    - use it when you want a connection-based socket
        A ----- B
                    // A and B exchange messages
                    // A and B terminate their connection when done
SOCK_DGRAM -> User Datagram Protocol (UDP)
    - individual messages as datagrams
        A --> B
        B --> A
                    // 2 seperate examples of datagrams
                    
TCP Sockets                                                                 UDP
    reliable -> detects packet loss                                         Sends one datagram
    connection based                                                        no order
    sequential                                                              no guarentee of arrival
        1, 2, 3, 4, 5                                                       almost real time - very fast
            // order sent by client is order recieved by the server         less network and PC stress. - weak hardware optimal?
    UDP is not, arrives in any order                                        use this when packet loss isnt the end of the world
    Byte-Stream                                                             
    Keeps up a connection                                                   
    Terminates when we dont want it any more
    Use this to have a nice connection between Internet devices 
    
CASE STUDY

Skype
UDP, A_INET
TCP, A_NET
calls are UDP, packet loss isnt the end of the world
but establishing a connection is TCP because critical

*------(TCP)-----*
A -(UDP)----- B
                                      
"""

import socket
import threading


# returns one of the kinds of local IPs
HOST = socket.gethostbyname(socket.gethostname())
PORT = 4545
ADDR = (HOST, PORT)  # assign a tuple
HEADER = 64
FORMAT = "ascii"
DISCONNECT_MESSAGE = "!DISCONNECT"

# this is a TCP Socket
# server is just used for accepting connections. It doest talk to clients
# # To make it a server, we have to bind() this to a HOST and a PORT
# always have to specify a private (local) IP Address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# server.listen(5) # before rejecting connections.

# NOTE: Its possible to connect clients through this server. Client A can see Client B
# youd have to do a global message list where you can see queues and stuff. its complicated but powerful


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)  # blocking
        if msg_length:  # if not none
            msg_length = int(msg_length[:4])
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg recieved".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()  # blocking
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIOINS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
print(f"[STARTING] host: {HOST}, port: {PORT}")
start()
