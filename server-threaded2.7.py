"""
Multi-threaded server.  Once a connection is accepted, a new 
thread is created to serve the client.
"""
import random
import socket
from thread import start_new_thread
import time

PORT = 1234
host = '127.0.0.1'  #localhost
#host = socket.gethostname()  #return this machine's hostname

wsdl = []  #array to hold wsdl addresses

#each new thread executes this function
def contacted(clientsocket):
    #receive string from client
    mssg = clientsocket.recv(1024)
    if (mssg[0:4] == 'http'):
        wsdl.append(mssg)
        print('wsdl array has: ')
        for addr in wsdl:
            print(addr)
    else:

   #    if(mssg='RequestForService'):
        r = random.randint(0,len(wsdl)-1)
        print("length of wsdl array: ", len(wsdl), " random value picked: ", r)
        wsdl_response = wsdl[r]
        clientsocket.send(wsdl_response)

    #delay added to test multi-threading parallelism
    #time.sleep(1)
    #send reverse message to the client
    #clientsocket.send(mssg_reverse)
    clientsocket.close()

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
    #multi-threading by start a new thread, which executes the argument's function
    start_new_thread(contacted, (clientsocket,))

s.close()


