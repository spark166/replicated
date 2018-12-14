import socket
import time
#from thread import start_new_thread


PORT = 1234  #port numbers < 1024 are reserved
host = '127.0.0.1'  #localhost addr, a standard loop back
#host = socket.gethostname()

wsdl = []  #an array to hold wsdl addresses

#create a socket object with IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to host addr and port
s.bind((host, PORT))
#listen to socket, queue as many as 8 connect requests
s.listen(8)

while True:
    #accept connection requests, this method is blocking
    (clientsocket, addr) = s.accept()
    print "Accepted connection from ", addr

    mssg = clientsocket.recv(1024)
    
    if (mssg[0:4] == 'http'):
        wsdl.append(mssg)
        print('wsdl length: ', len(wsdl))
        for addr in wsdl:
            print(addr)
    
    time.sleep(1)
    #send reverse message to the client
    #clientsocket.send(mssg_reverse)
    clientsocket.close()

s.close()



