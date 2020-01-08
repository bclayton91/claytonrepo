import xml.etree.ElementTree as ET
stream = open("people.xml")
xml = ET.parse(stream)
root=xml.getroot()
for e in root:
    print(ET.tostring(e))
    print("")
    print(e.get("Id"))