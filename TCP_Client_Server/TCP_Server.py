from socket import *
# enter command: ss -tl4 on command line to see if the serverPort that we would like to use(in this case 12000) is avaliable
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1',serverPort))
serverSocket.listen(1)
print('the server is ready to receive.')
try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024).decode() #receive the sentence from the client
        uppercaseSentence = sentence.upper()
        connectionSocket.send(uppercaseSentence.encode()) #send the uppsercase sentence back to the client
        connectionSocket.close()
except KeyboardInterrupt:
    print("\nServer is shutting down...")
# finally:
#     serverSocket.close()