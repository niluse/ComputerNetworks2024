from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
    sentence = input('Type in the sentence you would like to be uppercased: ')
    clientSocket.send(sentence.encode())
    uppercaseSentence = clientSocket.recv(1024)
    print('From the server:', uppercaseSentence.decode())
except ConnectionRefusedError:
    print("The server is unavailable. Please check the server address and port.")
except BrokenPipeError:
    print("The connection to the server was lost. Please try again.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    clientSocket.close()
