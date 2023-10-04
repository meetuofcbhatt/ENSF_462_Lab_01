from socket import *

name = input("User 1 Name: ")
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Client Socket Connected.")

clientSocket.send(name.encode())
server_name = clientSocket.recv(1024).decode()
print("User 2 Name: " + server_name)

while(True):
    sentence = input(name + ": ")
    clientSocket.send(sentence.encode())
    
    if sentence == "bye":
        break

    server_res = clientSocket.recv(1024).decode()
    print(server_name + ": "+ server_res)

    if server_res == "bye":
        break

print("Closing Client Socket.")
clientSocket.close()