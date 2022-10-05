from dzialanie import GlowneDzialanie

class Zamkniecie(GlowneDzialanie):

    def noweotwarcie(self):

        return super(Zamkniecie, self).noweotwarcie() + \
               "to jest metoda reprezentująca zamknięcie procesu\n"
