from datetime import date

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @classmethod
    def form_birth_day(cls,name,year):
        return cls(name,date.today().year - year)
    
    @staticmethod
    def isAdult(age):
        return age>18
