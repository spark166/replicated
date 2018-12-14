from zeep import Client
import socket  #socket library

PORT = 1234
host = '127.0.0.1'  #localhost
#host = socket.gethostname()  #return a hostname of this machine

#create a socket object with IPv4 and TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to a server with host address and specified port
s.connect((host, PORT))
#prompt for a user input
mssg = 'RequestForService'
#send the user input to the server
s.send(mssg)
#receive and print to a screen
wsdl_received = s.recv(1024)
print('received the following WSDL: ', wsdl_received)

s.close()


#generate a SOAP client using the received WSDL
client = Client(wsdl_received+'?wsdl')
result = client.service.helloName('AOS 621 Project')
print(result)

#assert result == 62.137
