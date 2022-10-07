odp = input("Czy Ziemia jest płaska? Chcesz znac odpowiedź według Filozofa? (t/n): ")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    return  "Tak!Ziemia jest płaska."

#definiujemy metaklasę

class SednoOdpowiedzi(type):

    def __init__(cls,nazwa,dziedziczenie,attrs):
        if required:
            cls.odpowiedz = odpowiedz

class Arystoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

fil1 = Arystoteles()
print(fil1.odpowiedz())

fil2 = Platon()
print(fil2.odpowiedz())

fil3= SwTomasz()
print(fil3.odpowiedz())
