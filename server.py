import socket
from _thread import *
import sys

server = "192.168.1.3"
port = 5555

# Initializing Socket
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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0), (100,100)]
# conn = connection
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    # Continue running while client is still connected
    while True:
        try:
            # 2048 stands for how many bits of information to receive from connection
            # If error occurs when running, just increase the 2048 number
            # The larger the size is, the longer it takes to receive info
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data


            # Decode information
            # reply = data.decode("utf-8")

            # If, cannot get info from client disconnect and break
            # else, print
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Received: ", data)
                print("Sending: ", reply)

            # Encode string reply into byte object
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
# Continuously looking for connections
while True:
    # String connection and address(IP)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1