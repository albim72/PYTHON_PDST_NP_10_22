#import dane
#import dane as dn

from dane import book
from funkcje import biblioteka, hx

#from miasto import Miasto
from stolica import Stolica, Miasto

print(book)
print(book["tytul"])

print(hx(6,9))

print(biblioteka("Gniezno",34,book['tytul']))

m = Miasto(56,"Zamość","lubelskie")
m.print_miasto()

s = Stolica(1,"Warszawa","mazowieckie","Jan Kot")
s.print_miasto()
s.prezydentinfo()
