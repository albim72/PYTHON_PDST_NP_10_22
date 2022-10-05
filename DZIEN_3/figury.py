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


