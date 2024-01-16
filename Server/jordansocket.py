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

HOST = "0.0.0.0"
# 192.168.0.#    // other examples
# 172.#.#.#
PORT = 1337
# pick stuff thats not commonly used (low numbers)
# the client and the server port have to be the same

# this is a TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server is just used for accepting connections. It doest talk to clients
server.bind((HOST, PORT))  # assign a tuple
# To make it a server, we have to bind() this to a HOST and a PORT
# always have to specify a private (local) IP Address

server.listen(5)  # how many connections to accept before rejecting connections.
# optional

# endless loop
while True:
    communication_socket, address = server.accept()
    # when the server.accept method triggers
    # returns address of the client making the connection
    # and a socket that we can use to talk to the client
    # NOTE: we do not use the server variable to talk to client, it needs to be the object from accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode("ascii")
    # we have to decode the string
    # client server have to speak the same language
    print(f"Message from client is: {message}")
    communication_socket.send(f"my data from the MID... blah blah blah").encode("ascii")
    # this is probably whats happening
    communication_socket.close()
    # optional, can leave alive to send messages
    print(f"Connection with {address} ended!")
