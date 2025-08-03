import socket
import threading

HOST = '127.0.0.1' # Localhost
PORT = 5555 # Arbitrary non-privileged port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message, sender = None):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, sender=client)
        except:
            index = clients.index(client)
            clients.remove(client) 
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat.'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive_connections():
    print(f"Server is running on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} has joined the chat.'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()