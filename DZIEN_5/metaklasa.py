class MojaMeta(type):

    def __new__(klaska, nazwaklasy, dziedziczone, atrybuty):
        print(f"nazwa klasy: {nazwaklasy}")
        print(f"klasy dziedziczone: {dziedziczone}")
        print(f"atrybuty: {atrybuty}")
        return type.__new__(klaska,nazwaklasy, dziedziczone, atrybuty)

class Startowa:
    pass

class Druga(Startowa, metaclass=MojaMeta):
    pass

class Trzecia(Druga):
    pass


s = Startowa()

d = Druga()

t = Trzecia()
