
from asyncore import write
import socket 
import threading
import os
os.system('cls' if os.name == 'nt' else 'clear')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ("Enter IPv4 of server you're trying you connect to. Make sure there are no mistakes in the ip example: 111.111.1.111 ")
Server_IP= input(": ")

print ("Now enter the port.")
PORT= int(input(": "))

client.connect((Server_IP, PORT))
print("You have been connected")
nickname = input("Choose a nickname: ")

def receive():
    while True:
        try: 
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        
def write():
    while True:
        message = nickname +": " + input("")
        client.send(message.encode('ascii'))
        if message == nickname +": " + "clear":
            os.system('cls')

    
receive_thread = threading.Thread(target=receive)
receive_thread.start()


write_thread= threading.Thread(target=write)
write_thread.start()