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
