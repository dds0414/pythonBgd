
import zipfile
from xml.dom import minidom

document = zipfile.ZipFile('word/4.docx')
xml_content = document.read('word/document.xml')
reparsed = minidom.parseString(xml_content)
print reparsed.toprettyxml(indent="  ", encoding="utf-8")
