animal = ("pies","kot","papuga","pies","mysz","koń","pies")
print(animal)
print(type(animal))

print(animal[1:3])
print(animal.index("papuga"))
print(animal.count('pies'))

if "papuga" in animal:
    print("Tak! papuga to zwierz....")

if "budynek" in animal:
    print("Błędne dane...")

print("papuga" in animal)

anim2 = ("pająk","ryba")

animal = animal + anim2

print(animal)

ob = ["obiekt77",77,0,False,"Toruń",99.99,"abc"]

mojakrotka = tuple(ob)

print(mojakrotka)
print(type(mojakrotka))

#zmodyfikuj krotkę:
#usuń wartość 77, zamień "Toruń" na "Kielce"
#wstaw na pozycję o indeksie 2 wartość -0.006
#wstaw na końcu wartość 1000
#wyświetl krotkę

mojalista = list(mojakrotka)
mojalista.remove(77)
it = mojalista.index("Toruń")
print(it)
mojalista[it] = "Kielce"
mojalista.insert(2,-0.006)
mojalista.append(1000)

mojakrotka = tuple(mojalista)
print(mojakrotka)
print(type(mojakrotka))
