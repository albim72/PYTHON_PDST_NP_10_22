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

    def bmi(self):
        return self.waga/(self.wzrost/100)**2

    def opis_bmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <= 25:
            return "waga prawidłowa"
        elif self.bmi() <= 30:
            return "nadwaga"
        else:
            return "otyłość"
        
    def policz_ppm(self,plec):
        if plec == "k":
            return 655.1 + 9.563 * self.waga+1.85 * self.wzrost - 4.676 * self.wiek
        elif plec == "m":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "podaj k lub m!"


p1 = Osoba("Jan",34,178,108)
p1.print_osoba()
print(f"wiek za 10 lat: {p1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({p1.czypracownik()})")
print(f"bmi ciała wynosi: {p1.bmi():.2f}, opis: {p1.opis_bmi()}")

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


class Pracownik(Osoba):

    #konstruktor z dziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy,wynagrodzenie):
        super().__init__(imie,wiek,wzrost,waga)
        self.firma = firma
        self.stanowisko = stanowisko
        self.latapracy = latapracy
        self.wynagrodzenie = wynagrodzenie

    def print_pracownik(self):
        print(f"dane pracownika -> firma: {self.firma}, stanowisko pracy: {self.stanowisko}, lata pracy: {self.latapracy}, "
              f"wynagrodzenie: {self.wynagrodzenie} zł")

    def czypracownik(self):
        return True

print("______________________________________")
e1 = Pracownik("Adam",41,179,88,"ABC","dyektor",12,10900)
e1.print_osoba()
e1.print_pracownik()
print(f"wiek za 10 lat: {e1.wiekza10lat()}")
print(f"czy osoba jest pracownikiem? ({e1.czypracownik()})")

class Sport:

    def __init__(self,dyscyplina,lata_upr,best_wynik):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.best_wynik = best_wynik

    def infosport(self):
        print(f"Dysycyplina: {self.dyscyplina}, lata uprawiania: {self.lata_upr}, życiówka: {self.best_wynik}.")


class Dodatkowa:
    pass


class Student(Pracownik,Sport,Dodatkowa):

    #konstruktor z wielodziedziczeniem
    def __init__(self,imie,wiek,wzrost,waga,nr_studenta,wydzial,kierunek,rok_stud,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lata_upr="",best_wynik=""):
        Pracownik.__init__(self,imie,wiek,wzrost,waga,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,best_wynik)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_stud = rok_stud


    def print_student(self):
        print(f"student nr {self.nr_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, "
              f" rok studiów: {self.rok_stud}.")

    def czypracownik(self):
        return self.firma != ""

    # def czypracownik(self):
    #     if self.firma == "":
    #         return False
    #     else:
    #         return True
print("___________________Student __________________")

s1 = Student("Olaf",22,176,79,545435,"Matematyka,Fiyka i Informatyka","Informatyka",3)
s1.print_osoba()
s1.print_student()
print(f"wiek za 10 lat: {s1.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({s1.czypracownik()})")


print("________________Student -> Pracownik_____________________")

s2 = Student("Olga",23,170,58,97755,"Wydział Budowlany","Architektura",4,"XYZ","pomocnik architekta",1,2700)
s2.print_osoba()
s2.print_pracownik()
s2.print_student()
print(f"wiek za 10 lat: {s2.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({s2.czypracownik()})")


print("________________Student -> Sportowiec_____________________")

s3 = Student("Robert",22,180,76,454656,"Wydział Nauk Społecznych","Socjologia",3,dyscyplina="biegi ultra", lata_upr=5,
             best_wynik="102km -> 18h 56min 23s")
s3.print_osoba()
s3.print_student()
s3.infosport()
print(f"wiek za 10 lat: {s3.wiekza10lat()}")
print(f"czy student jest pracownikiem? ({s3.czypracownik()})")
print(f"bmi ciała wynosi: {s3.bmi():.2f}, opis: {s3.opis_bmi()}")



