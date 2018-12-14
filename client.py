from zeep import Client
import socket  #socket library
import os

PORT = 12345
host = '127.0.0.1'  #localhost
#host = '130.85.251.172' 
replica = '127.0.0.1'
#host = socket.gethostname()  #return a hostname of this machine

mssg = 'Request Add'

# ping if registry is up
response = os.system("ping -c 1 " + host)
if response == 0:
  print('registry at '+host+ ' is up.')
  registry = host
else:
  print ('registry at '+host+' is down!')
  registry = replica

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

#assert result == 62.137
