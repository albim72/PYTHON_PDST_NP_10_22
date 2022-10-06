from pojzad import Pojazd

class Samochod(Pojazd):

    def __init__(self,marka,model,rok_prod,rodzaj_napedu,kolor,poj,moc,klima):
        super().__init__(marka,model,rok_prod,rodzaj_napedu,kolor)
        self.poj = poj
        self.moc = moc
        self.klima = klima

    #getters

    def get_poj(self):
        return self.poj

    def get_moc(self):
        return self.moc

    def get_klima(self):
        return self.klima

    #setters

    def set_moc(self,moc):
        self.moc = moc

    def set_poj(self,poj):
        self.poj = poj

    def set_klima(self,klima):
        self.klima = klima

    def vmax(self):
        if self.get_poj() <= 1.0:
            return 140
        elif self.get_poj() <= 1.5:
            return 160
        elif self.get_poj() <= 1.8:
            return 190
        elif self.get_poj() <= 2.0:
            return 210
        elif self.get_poj() <= 2.4:
            return 250
        else:
            return "powyżej 250"

    def naped(self):
        return f"Rodzaj napędu {self.get_rodzaj_napedu()} -> pojemność silnika: {self.get_poj()} l," \
               f" moc[kM]: {self.get_moc()} "
