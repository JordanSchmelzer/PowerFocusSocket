import socket

HOST = "localhost"  # this is the IP of the server (the Powerfocus)
PORT = 4545
# the public IP

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))  # pass tuple
# we dont bind the socket to the host, port like last time. instead, just connect to host server.

socket.send("Hello World!".encode("ascii"))
print(socket.recv(1024).decode("ascii"))
