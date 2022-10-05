from abc import ABCMeta, abstractmethod

class IPojzad:

    __metaclass__ = ABCMeta

    @abstractmethod
    def spalanie(self,litry,odl):raise NotImplementedError

    @abstractmethod
    def kosztyprzejzadu(self,litry,odl,cena_l):raise NotImplementedError
