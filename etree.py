
import xml.etree.ElementTree as ET

tree = ET.parse('wsdl/Hello.wsdl')
root = tree.getroot()
print(root.tag)

for child in root:
    print(child.tag, child.attrib)

#print(root[1].attrib)

#for addr in root.iter('wsdlsoap:address'):
#    print(addr.tag, addr.attrib)

#for addr in root.iter('wsdl:service'):
#    print(addr.tag, addr.attrib)

print(root.get('wsdlsoap:address'))
print(root.get('location'))
print(root.key())

for addr in root.iter('element'):
    print(addr.tag, addr.attrib)

for addr in root.findall('element'):
#    rank = country.find('rank').text
#    name = country.get('name')
    print(addr)
