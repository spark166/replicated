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
        print(wsdl_addr)

