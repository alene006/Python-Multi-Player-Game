import socket
from _thread import *
import sys

server = "192.168.1.3"
port = 5555

# Initializng Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding Server and Port to Socket
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# Listen for connections
# Only want max of 2 connections for this app
s.listen(2)
print("Waiting for a connection, Server Started")

# conn = connection
def threaded_client(conn):

    reply = ""
    # Continue running while client is still connected
    while True:
        try:
            # 2048 stands for how many bits of information to receive from connection
            # If error occurs when running, just increase the 2048 number
            # The larger the size is, the longer it takes to receive info
            data = conn.recv(2048)

            # Decode information
            reply = data.decode("utf-8")

            # If, cannot get info from client disconnect and break
            # else, print
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            # Encode string reply into byte object
            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()
# Continuously looking for connections
while True:
    # String connection and address(IP)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))