def powitanie():
    print("załóż nowe konto")
    print("opłać abonament")
    print("zaloguj się")


powitanie()
powitanie()

#komentowanie/odkomentowanie wielu linii: zaznacz blok, wciśnij kobinajcję: CTRL + /

# for _ in range(1,26):
#     powitanie()

for i in range(1,26,3):
    print("____",i,"____")
    powitanie()
