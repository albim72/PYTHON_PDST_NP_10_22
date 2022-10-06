from pojzad import Pojazd

class Rower(Pojazd):

    def __init__(self,marka,model,rok_prod,rodzaj_napedu,kolor,przerzutka,waga_ramy,blotniki):
        super().__init__(marka,model,rok_prod,rodzaj_napedu,kolor)
        self.przerzutka = przerzutka
        self.waga_ramy = waga_ramy
        self.blotniki = blotniki

    # getters

    def get_przerzutka(self):
        return self.przerzutka

    def get_waga_ramy(self):
        return self.waga_ramy

    def get_blotniki(self):
        return self.blotniki

    #setters

    def set_przerzutka(self,przerzutka):
        self.przerzutka = przerzutka

    def set_waga_ramy(self,waga_ramy):
        self.waga_ramy = waga_ramy

    def set_blotniki(self,blotniki):
        self.blotniki = blotniki


    def daneroweru(self):
        return f"marka: {self.get_marka()},model: {self.get_model()},rok_prod: {self.get_rok_prod()}," \
               f" waga_ramy: {self.get_waga_ramy()} kg"

    def naped(self):
        return f"rodzaj napędu: {self.get_rodzaj_napedu()}, przerzutka: {self.get_przerzutka()}"

