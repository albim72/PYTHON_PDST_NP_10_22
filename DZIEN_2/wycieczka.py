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
