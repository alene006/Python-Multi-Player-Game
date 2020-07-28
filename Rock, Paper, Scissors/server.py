import socket
from _thread import *
import pickle
from .game import Game


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

connected = set()
games = {}
idCount = 0

# conn = connection
def threaded_client(conn, p, gameId):
    pass

# Continuously looking for connections
while True:
    # String connection and address(IP)
    conn, addr = s.accept()
    print("Connected to: ", addr)

    # Keep track of how many people have connected to server
    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2  # Keep track of how many games are needed

    # Checking for pairs, if no pair (idCount % 2 == 1), create new game
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn))