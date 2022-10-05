from zamkniecie import Zamkniecie

zm = Zamkniecie()
wynik = zm.noweotwarcie()
print(wynik)
f = open("log_procesA.txt","a",encoding="utf-8")
f.write(wynik)
f.close()
