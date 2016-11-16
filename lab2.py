import socket



host = ''
port = 6500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
    
#can listen 5 coonections
s.listen(5)


while True:
    #build the connection
    conn, addr = s.accept();

    try:
        message = conn.recv(2048).decode('utf-8')
        print (message)
        #get the file
        file = message.split()[1]
        #get the version
        version = message.split()[2]
        
        f = open(file[1:])
        #read the data and output
        data = f.read()
        #print(data)
        #close the file
        f.close()
        
        if(version != 'HTTP/1.1'):
            error = '505 HTTP Version Not Supported'
            print(error)
            conn.send(error.encode('utf-8'))
            conn.close()
        else:
            #send data to the client
            outputdata = '\nHTTP/1.1 200 OK \n\n'
            conn.send(outputdata.encode('utf-8'))
            conn.sendall(data.encode('utf-8'))

            conn.close()

        
    except IOError:
        error2 = '\nHTTP/1.1 404 Not Found \n\n'
        conn.send(error2.encode())
        print ('FILE NOT FOUND')
        conn.close()
                  
    conn.close()

 # First I import the socket library, and then get the socket object s.
 # Bind the socket with host and port('' means any host and port 6500)
 # Since up to 5 connections can be allowed to wait in a queue, so the socket can listen to 5 connections
 # using s.listen(5)
 # Then make a while loop and start accepting request from client(using conn, addr = s.accept();)
 # After that, we retrieve the message and determine the specific file being requested
 # if the file exits
 # then test if the version of the http is compatible. If it's not 'HTTP/1.1', then return 505 HTTP Version Not Supported
 # and use conn.send(error.encode('utf-8') to send the message to the client
 # If the version is compatible, then we send the file to the client
 # then we close the connection and wait for another request
 # If the file does not exit, then we send the error message '404 Not Found' to the client
 # then close the connection
 # wait for the next request
 # I also used the terminal to test the server(telnet localhost 6500), and I put a data.txt file under the same folder as the server program
 # after the connection is made, I made another request from the brower
 # After the request from the terminal is finished, the server will handle the request from the brower
 


 
