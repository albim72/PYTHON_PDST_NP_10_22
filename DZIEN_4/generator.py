#przykład nr 1

def liczby():
    for i in range(11):
        yield i*2

for wynik in liczby():
    print(wynik)
