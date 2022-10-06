#przypadek nr 1

def powitanie(imie):
    return f"Witaj serdecznie {imie}!"

def procenty(imie):
    return f"Uczestnik konkursu {imie} - wyniki: "

def osoba(funkcja,imie,lpunktów):
    return f"{funkcja(imie)}, punkty konkursowe: {lpunktów}"

print(osoba(powitanie,"Roman",78))
print(osoba(powitanie,"Ola",81))

print(osoba(procenty,"Roman",78))
print(osoba(procenty,"Ola",81))


#przypadek nr 2

def egzamin(jesli):
    def zaliczony():
        return "Gratulacje, zdanego egzaminu!"
    def oblany():
        return "Przykro mi, następnym razem będzie lepiej!"
    if jesli == "tak":
        return zaliczony
    else:
        return oblany

print(egzamin("tak")())
print(egzamin("nie")())
print(egzamin("blabla")())


#przypadek nr 3

def startstop(funkcja):

    def wrapper():
        print("startowanie aplikacji.....")
        funkcja()
        print("zamykanie procesu aplikacji...")
    return wrapper
def zawijanie():
    print("zawijanie czekoladek w sreberka...")

print("________________________________")
z = startstop(zawijanie)
z()

print("________________________________")
@startstop
def bieganie():
    print("bieganie tu i tam....")

bieganie()
