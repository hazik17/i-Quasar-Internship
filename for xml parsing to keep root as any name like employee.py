import xml.etree.ElementTree as ET
mytree = ET.parse('employee.xml')
myroot = mytree.getroot()
print(myroot)