from abc import ABC,abstractmethod

class Pojazd(ABC):

    def __init__(self,marka,model,rok_prod,rodzaj_napedu,kolor):
        self.marka = marka
        self.model = model
        self.rok_prod = rok_prod
        self.rodzaj_napedu = rodzaj_napedu
        self.kolor = kolor

    #getters

    def get_marka(self):
        return self.marka

    def get_model(self):
        return self.model

    def get_rok_prod(self):
        return self.rok_prod

    def get_rodzaj_napedu(self):
        return self.rodzaj_napedu

    def get_kolor(self):
        return self.kolor

    #setters

    def set_marka(self,marka):
        self.marka = marka

    def set_model(self,model):
        self.model = model

    def set_rok_prod(self,rok_prod):
        self.rok_prod = rok_prod

    def set_rodzaj_napedu(self,rodzaj_napedu):
        self.rodzaj_napedu = rodzaj_napedu

    def set_kolor(self,kolor):
        self.kolor = kolor

    @abstractmethod
    def naped(self):raise NotImplementedError
