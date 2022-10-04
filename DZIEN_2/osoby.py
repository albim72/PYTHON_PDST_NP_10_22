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

    
    p1 = Osoba("Jan",34,178,108)
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")

print("___________________________________________________")


p2 = Osoba("Olga",27,165,57)
p2.kolor_oczu = "niebieskie"
p2.print_osoba()
print(f"wiek za 10 lat: {p2.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p2.czypracownik()})")

print("___________________________________________________")
p1.print_osoba()
p3 = Osoba("Karol",40,168,70)
p3.print_osoba()
