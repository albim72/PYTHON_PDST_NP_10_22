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
person1 = Person('Roman',21)
person2 = Person.from_birth_day('Leon',1998)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))

#print(person1.isAdult())
print(Person.from_birth_day('Ola',24))
