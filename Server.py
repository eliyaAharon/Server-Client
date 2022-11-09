import socket
import datetime
import random


def convert_date():
    x = datetime.datetime.now()
    w = str(x)
    return w


# create server socket
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8200))
server_socket.listen()

print("Server is up and running!")

(client_socket, client_adress) = server_socket.accept()

print("Client connected!")
x = ""
flag = True
while flag:
    data = client_socket.recv(1024).decode()
    if data == "Time":
        x = convert_date()
    if data == "Name":
        x = "Eliya Aharon"
    if data == "Rand":
        num = random.randint(0, 10)
        x = str(num)
    client_socket.send(x.encode())
    if data == "Exit":
        flag = False

server_socket.close()
client_socket.close()
