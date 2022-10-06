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
