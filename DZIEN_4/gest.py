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
        print("*****dodano nową książkę****")
        print(f"tytuł: {self.tytul}, autor: {self.autor}")


ks1 = Book(1,"Wiedźmin","Andrzej Sapkowski","Iskra",270,"Fantasy")
