#funkcja wysokiego rzędu filtrująca według warunku zewnętrznego
#Przykład 1

def filtrowanie(tablica,test):
    pozytywne = []
    for element in tablica:
        if (test(element)): #warunek ten oznacza że funkcja test() zwraca wartość True, czyli warubek jest spełniony
            pozytywne.append(element)
    return pozytywne

#funckja filtrowanie ostatecznie zwraca listę[]

def czyToSuperLiczba(liczba):
    return liczba>100

danetestowe = [2,45,6,107,100,99,-99,-190,234,89,200]
ddtest = {34,119,8,101,567,23}
sltest = {1:23,211:656,2899:155}

print(filtrowanie(danetestowe,czyToSuperLiczba))
print(filtrowanie(ddtest,czyToSuperLiczba))
print(filtrowanie(sltest,czyToSuperLiczba)) #problem z odczytem value()

#jak napisać funkcję, która obsłuży słownik i jego wartości a nie klucze...

#funckja mapująca na podstawie działania opisanego inną funkcją....
#Przykład 2

#parametr transformacja jest funkcją!!!
def mapowanie(dane,tranformacja):
    nowe_wart = []
    for element in dane:
        nowe_wart.append(tranformacja(element))
    return nowe_wart

def transformata_obl(nb):
    return (nb+2)**2

#pomniejsz 3-krotnie każdą wartość zestawu danych
def pomniejszanie(nb):
    return nb/3
print(mapowanie(danetestowe,transformata_obl))
print(mapowanie(ddtest,transformata_obl))
print(mapowanie(sltest,transformata_obl))

print(mapowanie(danetestowe,pomniejszanie))
print(mapowanie(ddtest,pomniejszanie))
print(mapowanie(sltest,pomniejszanie))
