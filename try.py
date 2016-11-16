from socket import *

#IP version 4, TCP protocol
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket

serverAddr = ('', 8787)

serverSocket.bind(serverAddr)
print ('socket bind complete')

serverSocket.listen(2);
print ('Socket now listening')

while True:
    #Establish the connection
    print ('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024)
        print (message)

        filename = message.split()[1]
        print ('\nFILENAME: ' + filename + '\n')
        f = open(filename[1:])
        outputdata = f.read()
        print (outputdata)

        connectionSocket.send(b'\nHTTP/1.1 200 OK \n\n')
        #connectionSocket.sendall(outputdata)
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        connectionSocket.send(b'\nHTTP/1.1 404 Not Found \n\n')
        print ('FILE NOT FOUND')
        connectionSocket.close()

serverSocket.close()
