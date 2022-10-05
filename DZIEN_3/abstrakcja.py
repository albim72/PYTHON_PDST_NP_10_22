from abc import ABC,abstractmethod

class Prototyp(ABC):

    def __init__(self,x):
        self.x=x

    def informacja(self):
        return "to jest metoda nieabstrakcyjna klasy abstrakcyjnej"

    #metody abstrakcyjne

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*5


class ZwKlasa(Prototyp):

    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 1001

    def policz_x(self):
        return super().policz_x() + 3*self.y


zw = ZwKlasa(6,3)
print(zw.informacja())
print(zw.policz())
print(zw.policz_x())


