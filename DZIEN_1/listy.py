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

litery = ['a','b','c','d','e','f','g','h']
print("litery przed zmianą:",litery)

litery[2:7] = [99,21,101]
print("litery po zmianie:",litery)

litery_m = litery
litery_p = list(litery)
litery_q = litery[:]

print("litery przed zmianą:",litery)
print("litery_m przed zmianą:",litery_m)
print("litery_p przed zmianą:",litery_p)
print("litery_q przed zmianą:",litery_q)

litery[:] = [1001,1002,1003,1115,1118]
print("litery po zmianie:",litery)
print("litery_m po zmianie:",litery_m)
print("litery_p po zmianie:",litery_p)
print("litery_q po zmianie:",litery_q)


kolory = ['czarny','biały','czerwony','zielony','niebieski','zółty']

#utwórz dwie listy parz i nieparz
#do listy parz dodaj te kolory z listy kolory, które posiadają indeksy parzyste
#do listy nieparz dodaj te kolory z listy kolory, które posiadają indeksy nieparzyste

nb = [3,1,56,7,8,1112,54,6,7,9,758,9]

nl = nb[3:11:3]

print(nl)


parz = kolory[::2]
nieparz = kolory[1::2]

print(parz)
print(nieparz)

w1 = "kajak"
w2 = "pomarańcza"

#wypisz wyrazy w1 i w1 w szyku odwróconym znaków (czytanie od końca)

w11 = w1[::-1]
w22 = w2[::-1]

print(w1,"-",w11)
print(w2,"-",w22)
