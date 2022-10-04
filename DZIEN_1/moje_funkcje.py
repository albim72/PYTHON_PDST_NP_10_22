def powitanie():
    print("załóż nowe konto")
    print("opłać abonament")
    print("zaloguj się")


powitanie()
powitanie()

#komentowanie/odkomentowanie wielu linii: zaznacz blok, wciśnij kobinajcję: CTRL + /

# for _ in range(1,26):
#     powitanie()

for i in range(1,26,3):
    print("____",i,"____")
    powitanie()

#druga fuknkcja - funkcja z parametrami
def obywatel(nrtelefonu,kraj="Polska"):
    print("kraj pochodzenia:",kraj,", numer telefonu:",nrtelefonu)

obywatel(5345345435,"Rumunia")
obywatel(5654656546,"Laos")
obywatel(5656535565,"Boliwia")
obywatel(7876767677,"Norwegia")
obywatel(4363456566)

#trzecia funkcja - zasięg zmiennych

def gx(n):
    return n**5

f = 100
def policz(a,b,x):
    global f
    f = (a+b)*x + f + gx(b)
    return f
#f =250 - zmienna niedostępna dla programu ze względu na działanie zmiennej globalnej f zdefiniowanej w funkcji
print(policz(3,6,2))

wynik = policz(4.5,6.7,8)
print(wynik)
print(f)


#funkcja 4 -> opcjonalne parametry

def miasta(miasto3,miasto2="Toruń",miasto1="Kraków"):
    print("miasto tygodnia:",miasto1,", drugie miejsce:",miasto2,", trzecie miejsce:",miasto3)

miasta("Katowice","Gniezno","Gdańsk")
miasta("Katowice","Gniezno")
miasta("Katowice")
miasta("Gliwice",None,"Zamość")
miasta("Gliwice",miasto1="Zamość")
