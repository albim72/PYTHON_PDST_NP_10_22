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
