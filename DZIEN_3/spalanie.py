from abc import ABCMeta, abstractmethod

class IPojzad:

    __metaclass__ = ABCMeta

    @abstractmethod
    def spalanie(self,litry,odl):raise NotImplementedError

    @abstractmethod
    def kosztyprzejzadu(self,litry,odl,cena_l):raise NotImplementedError

#stwórz interfejs opcujący nowe metody IDanePojazdu
#stworz metody abstrakcyjne: opispojzadu() oraz silnik()


class IDanePojazdu:

    __metaclass__ = ABCMeta

    @abstractmethod
    def opispojazdu(self):raise NotImplementedError

    @abstractmethod
    def silnik(self):raise NotImplementedError


#zaimplementuj klasę  IDanePojazdu jako drugą klasę w klasie Pojazd
#w klasie Pojzad - stwórz konstruktor(marka,model,rocznik,rodzaj_silnika,poj,moc)
#zaimplementuj metodę -> opispojazdu() -> wypisz wartości konstruktora: marka,model,rocznik
#zaimplementuj metodę -> silnik() -> wypisz wartości konstruktora: rodzaj_silnika,poj,moc

#wyświelt dane pojazdu przed wyznaczeniem kosztów spalania
class Pojazd(IPojzad,IDanePojazdu):

    def __init__(self,marka,model,rocznik,rodzaj_silnika,poj,moc):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.rodzaj_silnika = rodzaj_silnika
        self.poj = poj
        self.moc = moc

    def spalanie(self, litry, odl):
        return litry*100/odl

    def kosztyprzejzadu(self, litry, odl, cena_l):
        return self.spalanie(litry,odl)*(odl/100)*cena_l

    def opispojazdu(self):
        print(f"Pojazd -> marka: {self.marka}, model: {self.model}, rocznik: {self.rocznik}")

    def silnik(self):
        print(f"Silnik -> rodzaj silnika: {self.rodzaj_silnika}, pojemność: {self.poj}, moc: {self.moc} kM")


p1 = Pojazd("Toyota","Avensis",2019,"Benzyna",2.0,150)
lt = float(input("podaj ile litrów paliwa spalił samochód podczas przejazdu: "))
odl = float(input("podaj długość trasy: "))
cn = float(input("podaj cenę za litr paliwa: "))

#opis pojazdu
p1.opispojazdu()
p1.silnik()
print(f"spalanie [l/100km] wynosi: {p1.spalanie(lt,odl):.2f}")
print(f"koszty przejazdu na trasie: {odl} km wynoszą {p1.kosztyprzejzadu(lt,odl,cn):.2f} zł")
