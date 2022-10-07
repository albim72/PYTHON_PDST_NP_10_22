from xml.dom.minidom import parse

dom = parse("dane.xml")
name = dom.getElementsByTagName('name')
kod = dom.getElementsByTagName('kod')

print(" ".join(t.nodeValue for t in name[0].childNodes if t.nodeType == t.TEXT_NODE))
print(" ".join(t.nodeValue for t in kod[0].childNodes if t.nodeType == t.TEXT_NODE))
