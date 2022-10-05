from miasto import Miasto

class Stolica(Miasto):

    def __init__(self,id,nazwa,woj,prezydent):
        super().__init__(id,nazwa,woj)
        self.prezydent = prezydent

    def prezydentinfo(self):
        print(f"prezydent Stolicy: {self.prezydent}")
