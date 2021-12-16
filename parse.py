import xml.etree.ElementTree as ET
mytree = ET.parse('Sample.xml')
myroot = mytree.getroot()
print(myroot)
