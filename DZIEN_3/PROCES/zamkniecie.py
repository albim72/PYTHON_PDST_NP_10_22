from dzialanie import GlowneDzialanie

class Zamkniecie(GlowneDzialanie):

    def noweotwarcie(self):
        super(Zamkniecie, self).noweotwarcie()
        print("to jest metoda reprezentująca zamknięcie procesu")
