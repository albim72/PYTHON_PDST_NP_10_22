from xml.etree.ElementTree import Element,SubElement,Comment
import xml.etree.ElementTree as ET
from prettyfy import pretty

#<autokomis>
# <samochod>...
#   ...
#   <wyp_dodatkowe>
#       ...
#   </wyp_dodatkowe>
# </samochod>
# <samochod>...</samochod>
# ...
# </autokomis>

top = Element("autokomis")
sam1 = SubElement(top,"samochod")

id = SubElement(sam1,"id")
id.text = 'sam1'

marka = SubElement(sam1,"marka")
marka.text = 'Subaru'

model = SubElement(sam1,"model")
model.text = 'Impreza'

poj = SubElement(sam1,"pojemnosc")
poj.text = '1.8'

cena = SubElement(sam1,"cena")
id.text = '61900'

wyp_dod = SubElement(sam1,"wyp_dodatkowe")

kolor = SubElement(wyp_dod,"kolor")
kolor.text = 'czarna perła'

pod = SubElement(wyp_dod,"poduszki")
pod.text = '4'

klima = SubElement(wyp_dod,"klima")
klima.text = 'GTR4535'

#drugi rekord -> sam2

sam2 = SubElement(top,"samochod")

id = SubElement(sam2,"id")
id.text = 'sam2'

marka = SubElement(sam2,"marka")
marka.text = 'Subaru'

model = SubElement(sam2,"model")
model.text = 'Outback'

poj = SubElement(sam2,"pojemnosc")
poj.text = '2.4'

cena = SubElement(sam2,"cena")
id.text = '126970'

wyp_dod = SubElement(sam2,"wyp_dodatkowe")

kolor = SubElement(wyp_dod,"kolor")
kolor.text = 'czerwony metallic'

klima = SubElement(wyp_dod,"klima")
klima.text = 'VBBN785'


print(pretty(top))

zapis = open("subaru.xml","a",encoding="utf-8")
zapis.write(pretty(top))
zapis.close()
