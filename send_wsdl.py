"""
A simple client, which establishes a TCP connection with a server.
Prompt for a user input, which is sent to the server. Then, waits
for a message from the server, which gets displayed.
"""
SERVICE_NAME = 'Hello '
PORT = 12345
#host = '127.0.0.1'  #localhost
host = '130.85.251.172'  #localhost

#host = socket.gethostname()  #return a hostname of this machine


import socket  #socket library
import sys

f = open('wsdl/Hello.wsdl', 'r+')
lines = [line for line in f.readlines()]
f.close()

#extract the wsdl address
for line in lines:
    tok = line.split('=')
    #print(tok)
    if (tok[0] == '         <wsdlsoap:address location'):
        tok2 = tok[1].split('"')
        wsdl_addr = tok2[1]
        #print(tok2)
        print('wsdl address extracted is: ', wsdl_addr)


#create a socket object with IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to a server with host address and specified port
s.connect((host, PORT))

#prompt for a user input
#mssg = raw_input("Enter message:")
#if len(mssg)==0:  #if the user input is empty
#    mssg=' '

#send wsdl address to the registry server
print ('sending the extracted wsdl address to registry')
mssg = SERVICE_NAME+wsdl_addr
print(mssg)
s.send(mssg)

#receive and print to a screen
#print s.recv(1024)

s.close()


