from zeep import Client
import socket  #socket library
import os
import pyping

PORT = 12345
PORT2 = 12346
#host = '127.0.0.1'  #localhost
host = '130.85.251.172' 
replica = '130.85.241.172'
#host = socket.gethostname()  #return a hostname of this machine

mssg = 'Request Hello'

# ping if registry is up
response = pyping.ping(host)
if response.ret_code == 0:
  print('registry at '+host+ ' is up.')
  registry = host
else:
  print ('registry at '+host+' is down!')
  registry = replica
  PORT = PORT2
  

#create a socket object with IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to a server with host address and specified port
s.connect((registry, PORT))
#send the user input to the server
s.send(mssg)
#receive and print to a screen
wsdl_received = s.recv(1024)
print('received the following WSDL from '+registry+': '+ wsdl_received)

s.close()

#generate a SOAP client using the received WSDL
client = Client(wsdl_received+'?wsdl')
result = client.service.helloName('AOS 621 Project')
print(result)