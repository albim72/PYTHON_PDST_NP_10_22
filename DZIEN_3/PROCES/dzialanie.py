from otwarcie import Otwarcie


class GlowneDzialanie(Otwarcie):

    def noweotwarcie(self):

        return super(GlowneDzialanie, self).noweotwarcie() + \
               "to jest główna część wykonawcza całego procesu\n"
