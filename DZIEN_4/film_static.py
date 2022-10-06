class Film:

    def __init__(self,tytul,gatunek):
        self.tytul = tytul
        self.gatunek = gatunek

    @staticmethod
    def cena_po_rabacie(cena,rabat):
        return cena*(1-rabat/100)

    @classmethod
    def cena_ze_zwyzka(self,cena,zw):
        return cena*(1+zw/100)


f1 = Film("Gwiezdne Wojny","SF")
print(f"cena wypożyczenia z rabatem: {f1.cena_ze_zwyzka(12,23)} zł")

print(f"hipotetyczna cena innego filmu: {Film.cena_po_rabacie(7,3)} zł")

#Film.cena_po_rabacie = staticmethod(Film.cena_po_rabacie)

print(f"hipotetyczna cena innego filmu: {Film.cena_po_rabacie(7,3)} zł")
print(f"hipotetyczna cena ze zwyzką: {Film.cena_ze_zwyzka(14,12)} zł")
