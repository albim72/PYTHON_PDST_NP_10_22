class Kwadrat:

    def __init__(self,bok):
        self.bok = bok

    def pole(self):
        return self.bok**2

class Prosotkat:

    def __new__(cls, szer:float, wys:float):
        if szer == wys:
            return Kwadrat(bok=szer)
        return object.__new__(Prosotkat)

    def __init__(self,szer:float, wys:float):
        self.szer = szer
        self.wys = wys

    def pole(self):
        return self.szer*self.wys

r1 = Prosotkat(12,8)
print(type(r1))
print(f"pole: {r1.pole()}")

r2 = Prosotkat(6,6)
print(type(r2))
print(f"pole: {r2.pole()}")
