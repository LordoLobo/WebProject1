import threading
import socket
import sys
import random
Local ='localhost'

HOST = socket.gethostbyname(socket.gethostname())
HOST = str(HOST)

PORT = random.uniform(10000, 60000)
PORT = int(PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

Commands = "In progress... onlinecheck, ban, kick, time..."
clients = []
nicknames = []

print("IPv4: " + str(HOST) + " Port: " + str(PORT))

def broadcast (message):
    for client in clients:
      client.send(message)
   
def handle (client):
  while True:
    try:
      message = client.recv(1024)
      broadcast(message)
    except:
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      broadcast((nickname + " has left the chat room!").encode('ascii'))
      print (nickname + " has left the chat room!")
      nicknames.remove(nickname)
      break



def receive ():
  while True:
    client, address = server.accept()
    print("Connected with " + str(address))
    
    client.send('NICK'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)
    
    print("Nickname of the client is " + nickname + "!")
    client.send('-Connected to the server-'.encode('ascii'))
    broadcast((nickname + ' has joined the chat!').encode('ascii'))
    
    
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()
print("server is listening...")
receive()