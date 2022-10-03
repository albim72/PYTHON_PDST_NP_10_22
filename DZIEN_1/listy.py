kraje = ["Polska","Norwegia","Kanada","Japonia","RPA","Islandia"]

print(kraje)
print(type(kraje))

print(kraje[1])
print(kraje[3])
print(kraje[2:5])

kraje.append("Turcja")
print(kraje)

kraje.remove("Kanada")
print(kraje)

del kraje[1]
print(kraje)

kraje.insert(3,"Finlandia")
print(kraje)

kraje[2] = "Brazylia"
print(kraje)

kraje.sort()
print(kraje)

liczby = [2,67,88,112,-88,78,123,112,0,5,-9,112,190]

liczby.reverse()
print(liczby)

liczby.sort()
print(liczby)

liczby.reverse()
print(liczby)

liczby.sort(reverse=True)
print(liczby)

nb = [34,12,-100]

liczby = liczby + nb
print(liczby)

liczby = liczby*3
print(liczby)


rasa = ["dalmatyńczyk","buldog angielski","husky"]
cenaras = [6000,7500,4500]

sklepzoo = [[rasa,"kot","papuga","szynszyla","mysz"],[cenaras,3000,9000,250,50]]

print(sklepzoo[0])
print(sklepzoo[0][0])
print(sklepzoo[0][0],", cena:",sklepzoo[1][0],"zł")
print(sklepzoo[0][0][1],", cena:",sklepzoo[1][0][1],"zł")
