class Book:

    def __init__(self,id,tytul,autor,wyd,lstron,gatunek):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.wyd = wyd
        self.lstron = lstron
        self.gatunek = gatunek
        self._info()


    def _info(self):
        print("*****dodano nową książkę*****")
        print(f"tytuł: {self.tytul}, autor: {self.autor}")

    def get_tytul(self):
        return self.tytul

    def get_autor(self):
        return self.autor

    def set_tytul(self,tytul):
        self.tytul = tytul

    def set_autor(self,autor):
        self.autor = autor

    def info_book(self):
        return f"Książka -> tytuł: {self.get_tytul()}, autor: {self.get_autor()}"


ks1 = Book(1,"Wiedźma","Andrzej Klin","Iskra",270,"Fantasy")
print(f"tytuł książki: {ks1.get_tytul()}")
print(f"autor książki: {ks1.get_autor()}")

ks1.set_autor("Andrzej Sapkowski")
ks1.set_tytul("Wiedźmin")

print("___________________________________________")

print(ks1.info_book())

class Seria(Book):

    def __init__(self,id,tytul,autor,wyd,lstron,gatunek,nazwa_serii,objetosc,lata):
        super().__init__(id,tytul,autor,wyd,lstron,gatunek)
        self.nazwa_serii = nazwa_serii
        self.objetosc = objetosc
        self.lata = lata

    def get_nazwa_serii(self):
        return self.nazwa_serii

    def set_nazwa_serii(self,nazwa_serii):
        self.nazwa_serii = nazwa_serii

    def info_seria(self):
        return f"Książka -> tytuł: {self.get_tytul()}, autor: {self.get_autor()}, " \
               f"nazwa serii: {self.get_nazwa_serii()}"


sr = Seria(23,"Silmarillion","Tytus Chałubiński","PWN",450,"Fantasy","Władca",3,"1949-1953")

print(f"tytuł książki: {sr.get_tytul()}")
print(f"autor: {sr.get_autor()}")
print(f"nazwa serii: {sr.get_nazwa_serii()}")

print("________________________________________________________")

sr.set_tytul("Drużyna Pierścienia")
sr.set_autor("J.R.R. Tolkien")
sr.set_nazwa_serii("Władca Pierścieni")

print(sr.info_seria())
