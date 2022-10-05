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
    
    
class TrzeciaKlasa(DrugaKlasa):
    
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d
    
    def print_abcd(self):
        print(f"Klasa TrzeciaKlasa -> a={self.a}, b={self.b}, c={self.c}, d={self.d}")

    def suma_elementow(self):
        return super().suma_elementow() + self.d
        
print("____Pierwsza Klasa____")
pk = PierwszaKlasa(4,7)
pk.print_ab()
print("____Druga Klasa____")
dk = DrugaKlasa(6,1,3)
dk.print_ab()
dk.print_abc()
print(f"suma elementów = {dk.suma_elementow()}")
print("____Trzecia Klasa____")
tk = TrzeciaKlasa(9,2,6,3)
tk.print_ab()
tk.print_abc()
tk.print_abcd()
print(f"suma elementów = {tk.suma_elementow()}")
    
