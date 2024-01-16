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

HOST = ""
PORT = ""

# this is a TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# To make it a server, we have to bind() this to a HOST and a PORT
# always have to specify a private (local) IP Address
