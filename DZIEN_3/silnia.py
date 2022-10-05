#n! = 1*2*....*n
#float ??
#double -> max 1.8E+308
#n?? n = 171!

import sys

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")

    wynik = 1
    for i in range(1,n+1):
        wynik*=i   #wynik = wynik*i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")

    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość argumentu funckji silnia n: "))
    sys.setrecursionlimit(10000)
    print(f"silnia z n = {n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z n = {n} wynosi: {silnia_rek(n)}")
except ValueError as df:
    print(df)
