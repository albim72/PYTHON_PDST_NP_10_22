from abc import ABCMeta, abstractmethod

class IPojzad:

    __metaclass__ = ABCMeta

    @abstractmethod
    def spalanie(self,litry,odl):raise NotImplementedError

    @abstractmethod
    def kosztyprzejzadu(self,litry,odl,cena_l):raise NotImplementedError

        
        
class Pojazd(IPojzad):

    def spalanie(self, litry, odl):
        return litry*100/odl

    def kosztyprzejzadu(self, litry, odl, cena_l):
        return self.spalanie(litry,odl)*(odl/100)*cena_l
