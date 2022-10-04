class Kolor:

    #opis stanu -> konstruktor klasy
    def __init__(self,id,nazwa):
        self.idkoloru = id
        self.nazwa = nazwa
        self.paleta = "Paleta X"

    #opis Zachowania - funkcje klasy: metody

    def print_kolor(self):
        print(f"kolor -> id: {self.idkoloru}, nazwa: {self.nazwa}")
