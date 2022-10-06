#przykład nr 1

def liczby():
    for i in range(11):
        yield i*2

for wynik in liczby():
    print(wynik)

    #przykład nr 2

def wznowienia():
    print("wstrzymuję działania")
    yield 101
    print("wznawiam działania")

    print("wstrzymuję działania")
    yield 199
    print("wznawiam działania")

    print("wstrzymuję działania")
    yield 1098
    print("wznawiam działania")

print("______________________________________")
for i in wznowienia():
    print(f"Zwrócono wartość: {i}")
