
import socket  #socket library
import sys

"""
A simple client, which establishes a TCP connection with a server.
Prompt for a user input, which is sent to the server. Then, waits
for a message from the server, which gets displayed.
"""
SERVICE_NAME = 'Hello '
PORT = 12345
#registry = '127.0.0.1'  #localhost
registry_hard = '130.85.241.172'  #######################registry address

#hostname = socket.gethostname()  #return a hostname of this machine


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

        hostname = socket.gethostname()    
        server_ip = socket.gethostbyname(hostname)    
        tomcat_addr = wsdl_addr[:7]+server_ip+wsdl_addr[16:]
        print('wsdl address to send is: ', tomcat_addr)

#create a socket object with IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to a server with registry address and specified port
s.connect((registry_hard, PORT))

#prompt for a user input
#mssg = raw_input("Enter message:")
#if len(mssg)==0:  #if the user input is empty
#    mssg=' '

#send wsdl address to the registry server
print ('sending the extracted wsdl address to registry')
mssg = SERVICE_NAME+tomcat_addr
print(mssg)
s.send(mssg)

#receive and print to a screen
#print s.recv(1024)

s.close()


