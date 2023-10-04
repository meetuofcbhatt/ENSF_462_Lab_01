from socket import *
name = input("User 2 Name: ")
serverPort = 12000
print("Starting Socket Connection.")
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1)
print('Socket Connection is Complete.')

connectionSocket, addr = serverSocket.accept()
client_name = connectionSocket.recv(1024).decode()
print("User 1 Name: " + client_name)
connectionSocket.send(name.encode())

while(True):
    
    client_res = connectionSocket.recv(1024).decode()
    print(client_name + ": " + client_res)
    if client_res == "bye":
        break
    
    sentence = input(name + ": ")
    connectionSocket.send(sentence.encode())

    if sentence == "bye":
        break

print("Closing Server Socket.")
connectionSocket.close()

    