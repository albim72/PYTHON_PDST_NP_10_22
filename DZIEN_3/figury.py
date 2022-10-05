from abc import ABC,abstractmethod

class Figura(ABC):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    @abstractmethod
    def policz_pole(self):
        pass


class Prostokat(Figura):

    def policz_pole(self):
        return self.a*self.b


class Trojkat(Figura):

    def policz_pole(self):
        return self.a*self.b/2


pr = Prostokat(5.6,7.8)
print(f"pole prostokąta wynosi: {pr.policz_pole():.2f}")

tr = Trojkat(6.8,5.9)
print(f"pole trójkąta wynosi: {tr.policz_pole():.2f}")


#Stwórz klasę Kolo dziedziczącą klasę Figura, policz pole koła dla promienia równego 5.5
#pole koła -> math.pi*a**2

class Kolo(Figura):

    def __init__(self,a):
        super().__init__(a,0)

    def policz_pole(self):
        return math.pi*self.a**2


kl = Kolo(5.5)
print(f"pole koła wynosi: {kl.policz_pole():.2f}")
