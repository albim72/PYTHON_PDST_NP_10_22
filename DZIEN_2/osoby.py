class Osoba:

    def __init__(self,imie,wiek,wzrost,waga):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.kolor_oczu = "brązowy"
        self.info()


    def info(self):
        print("tworzenie nowej instancji klasy Osoba...")


    def print_osoba(self):
        print(f"osoba -> imię: {self.imie}, wiek: {self.wiek} lat/a, wzrost: {self.wzrost} cm, "
              f"waga: {self.waga} kg, kolor oczu: {self.kolor_oczu}")

    def wiekza10lat(self):
        return self.wiek + 10
    
    def czypracownik(self):
        return False
