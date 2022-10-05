#n! = 1*2*....*n
#float ?? 
#double -> max 1.8E+308
#n?? n = 171!

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    
    wynik = 1
    for i in range(1,n+1):
        wynik*=i   #wynik = wynik*i
    return wynik

try:
    n = int(input("podaj wartość argumentu funckji silnia n: "))
    print(f"silnia z n = {n} wynosi: {silnia(n)}")
except ValueError as df:
    print(df)
