class Rodzic:

    def dzialanie_rodzica(self):
        print("Rodzic poucza Dziecko....")

class Dziecko(Rodzic):

    def __init__(self):
        print("Dziecko zostało utworzone przez Rodzica....")

    def dzialanie_dziecka(self):
        print("Dziecko słucha Rodzica")


child = Dziecko()

child.dzialanie_rodzica()
child.dzialanie_dziecka()
