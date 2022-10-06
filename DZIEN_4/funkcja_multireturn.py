#stwórz listę dwóch wartości [a,b]
#napisz fuknkcję ktra będzie liczyła podstawowe działania matematyczne
#funkcja ma zwracać kolekcję wszystkich wyników razem (dodawanie,odejmowanie,mnożenie,
# dzielenie,modulo, potęga)
#po wywołaniu funckji przekaż wyniki do wyizolowanych zmiennych i wypisz je na ekranie!


dane = []

def dzialania(d):
    dod = d[0] + d[1]
    odej = d[0] - d[1]
    mno = d[0]*d[1]
    dziel = d[0]/d[1]
    mod = d[0]%d[1]
    pot = d[0]**d[1]
    return dod,odej,mno,dziel,mod,pot

a = int(input("podaj wartość a: "))
b = int(input("podaj wartość b: "))
dane.append(a)
dane.append(b)
dod,odej,mno,dziel,mod,pot = dzialania(dane)

print(f"a={dane[0]}, b={dane[1]} -> \ndodawanie a+b: {dod}\n"
      f"odejmowane a-b: {odej}\n"
      f"mnożenie a*b: {mno}\n"
      f"dzielenie a/b: {dziel}\n"
      f"modulo a%b: {mod}\n"
      f"potęga a**b: {pot}\n")
