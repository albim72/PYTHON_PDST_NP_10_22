from otwarcie import Otwarcie

class GlowneDzialanie(Otwarcie):

    def noweotwarcie(self):
        super(GlowneDzialanie,self).noweotwarcie()
        print("to jest główna część wykonawcza całego procesu")
