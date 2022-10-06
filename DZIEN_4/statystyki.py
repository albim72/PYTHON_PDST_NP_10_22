liczby = [12,6,78,0,-88,1099,-456,23,69,101,-444,999,9,15,765]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    return minimum,maksimum,rozstep

wynik = pokaz_stat(liczby)
print(wynik)
print(type(wynik))

mini, maxi, roz = pokaz_stat(liczby)
print(f"Wartość maksymalna: {maxi}, wartość minimalna: {mini}, roztęp wynosi: {roz}")
