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
