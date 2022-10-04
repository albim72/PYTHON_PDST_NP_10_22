class Kolor:

    #opis stanu -> konstruktor klasy
    def __init__(self,id,nazwa):
        self.idkoloru = id
        self.nazwa = nazwa
        self.paleta = "Paleta X"

    #opis Zachowania - funkcje klasy: metody

    def print_kolor(self):
        print(f"kolor -> id: {self.idkoloru}, nazwa: {self.nazwa}")

        
#tworzenie obiektu
k1 = Kolor(23,"czerwony")
k2 = Kolor(12,"zielony")

k1.print_kolor()
k2.paleta = "Paleta A"
k2.print_kolor()
k3=Kolor(9,"seledyn")
k3.print_kolor()
