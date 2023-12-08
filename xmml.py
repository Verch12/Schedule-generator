import xml.etree.ElementTree as ET
tree = ET.parse('12.xml')
root = tree.getroot()

print (ET.tostring(root, encoding='utf-8').decode('utf-8'))