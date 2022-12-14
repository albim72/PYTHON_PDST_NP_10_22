#funkcja kwota(transport,nocleg_wyz,wycieczki,ubezp,inne,rabat) ->
#(transport + nocleg_wyz)*(1-rabat/100)+wycieczki+ubezp+inne

#pozwalaj tylko na wprowadzenie rabatu z zakresu (1-70%)
#blokuj roziwązanie dla innych wartości
#wartość 0 dla rabatu uczyńmy wartością domyślną parametru rabat (rabat=0)


def kwota(t,nw,w,u,i,rab=0):
    if rab>=0 and rab <= 70:
        return (nw+t)*(1-rab/100)+w+u+i
    else:
        return "podaj rabat mniejszy niż 71% lub większy od 0"

print("kwota do zapłaty",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,75),"zł")


#dla rabatu 0 wypisz -> kwota bazowa wynosi: kwota
#dla rabatów pozostałych -> dla rabatu x% kwota do zapłaty wynosi: kwota
print("***************************************")
rabs = [0,8,10,12,15,20,25]


#dodatkowo: zapisz kwoty które policzyliśmy dla każdego rabatu do tablicy wynik =[]

wynik = []
for r in rabs:
    kw = kwota (1700, 1230, 450, 200, 180, r)

    if r == 0:
        print ("cena bazowa do zapłaty wynosi:",kw,"zł")

    else:
        print ("dla rabatu:", r, "%, kwota do zapłaty wynosi:", kw,"zł")

    wynik.append(kw)


print (wynik)

result = [kwota(1700,1230,450,200,180,r) for r in rabs]
print(result)
