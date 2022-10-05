class PierwszaKlasa:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def print_ab(self):
        print(f"Klasa PierwszaKlasa -> a={self.a}, b={self.b}")

class DrugaKlasa(PierwszaKlasa):

    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c

    def print_abc(self):
        print(f"Klasa DrugaKlasa -> a={self.a}, b={self.b}, c={self.c}")

    def suma_elementow(self):
        return self.a+self.b+self.c


class SpecjalnaKlasa:

    def __init__(self,g,h):
        self.g = 2*g
        self.h = h-8

    def px(self):
        return 2*self.g-self.h

#Rozbuduj TrzeciaKlasa o dodtkowe dziedziczenie klasy SpesjalnaKlasa (wielodziedziczenie),
#konsekwentnie rozbuduj konstruktor
#zmień nazwę metody print_abcd() na print_abcdgh() i dopisz w wyniku dwa dodatkowe parametry g i h
#zmień wynik funckji suma_elementow dodając do aktualnego wyniku wynik działania funckji px()
#uzupełnij deklarację instancji tk

class TrzeciaKlasa(DrugaKlasa, SpecjalnaKlasa):

    def __init__(self,a,b,c,d,g,h):
        DrugaKlasa.__init__(self,a,b,c)
        SpecjalnaKlasa.__init__(self,g,h)
        self.d=d

    def print_abcdgh(self):
        print(f"Klasa TrzeciaKlasa -> a={self.a}, b={self.b}, c={self.c}, d={self.d}, g={self.g}, h={self.h}")

    def suma_elementow(self):
        return super().suma_elementow() + self.d + self.px()


print("____Pierwsza Klasa____")
pk = PierwszaKlasa(4,7)
pk.print_ab()
print("____Druga Klasa____")
dk = DrugaKlasa(6,1,3)
dk.print_ab()
dk.print_abc()
print(f"suma elementów = {dk.suma_elementow()}")
print("____Trzecia Klasa____")
tk = TrzeciaKlasa(9,2,6,3,17,8)
tk.print_ab()
tk.print_abc()
tk.print_abcdgh()
print(f"suma elementów = {tk.suma_elementow()}")
