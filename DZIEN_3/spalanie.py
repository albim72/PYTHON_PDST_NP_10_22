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

    


class Pojazd(IPojzad):

    def spalanie(self, litry, odl):
        return litry*100/odl

    def kosztyprzejzadu(self, litry, odl, cena_l):
        return self.spalanie(litry,odl)*(odl/100)*cena_l


p1 = Pojazd()
lt = float(input("podaj ile litrów paliwa spalił samochód podczas przejazdu: "))
odl = float(input("podaj długość trasy: "))
cn = float(input("podaj cenę za litr paliwa: "))

print(f"spalanie [l/100km] wynosi: {p1.spalanie(lt,odl):.2f}")
print(f"koszty przejazdu na trasie: {odl} km wynoszą {p1.kosztyprzejzadu(lt,odl,cn):.2f} zł")
