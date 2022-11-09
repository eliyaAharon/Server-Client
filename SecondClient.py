import socket

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 8820))
temp = str(input("Enter a masage to the server"))
my_socket.send(temp.encode())

data = my_socket.recv(1024).decode()

print("The server sent " + data)

my_socket.close()
