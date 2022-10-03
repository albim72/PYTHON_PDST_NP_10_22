#instrukcja warunkowa
a = 1
b = 1

if a>b:
    print("a jest większe niż b")
elif a==1 and b==1:
    print("przypadek specjalny: a=b=1")
elif a == b:
    print("a jest równe b")
else:
    print("a jest mniejsze niż b")

#instrukcja dostępna tylko w wersji 3.10 lub przyszłej
day = int(input("podaj nr dnia tygodznia (1-7): "))
match day:
    case 1:
        print("poniedziałek")
    case 2:
        print("wtorek")
    case 3:
        print("środa")
    case 4:
        print("czwartek")
    case 5:
        print("piątek")
    case 6:
        print("sobota")
    case 7:
        print("niedziela")
    case other:
        print("zły wybór -> tylko (1-7)")

#instrukcja iteracyjna

i = 1
while i<6:
    print(i)
    if i==7:
        break
    i+=1
else:
    print("ostatecznie i =",i)


owoce = ["jabłko","banan","malina","cytyryna","aronia"]

print(owoce)

for owoc in owoce:
    print(owoc)

cechy = ["kolorowy","elegancki","kosztowny","ładny"]
obiekty = ["budynek","samochód","ogród","płaszcz","przystanek"]

for x in cechy:
    for y in obiekty:
        print(x,y)

