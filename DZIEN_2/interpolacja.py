wiek = 56
miasto = "Opole"
imie = "Paweł"

osoba = "Dane osoby -> imię: {}, miasto: {}, wiek: {}."
print(osoba.format(imie,miasto,wiek))
osoba = "Dane osoby -> imię: {0}, wiek: {2}, miasto: {1}."
print(osoba.format(imie,miasto,wiek))

nazwa_firmy = "XYZ sp zoo"
stanowisko = "dyrektor"

print(f"Dane pracownika -> imię: {imie}, nazwa firmy: {nazwa_firmy}, stanowisko :{stanowisko}"
      f", wiek osoby: {wiek}, miasto: {miasto}")

j = 10.4564356
print(f"zokrąglona wartość: {j:11.2f}")

nz = "G789"
w = 86.467743

formatowanie = '%-30s = %.2f' %(nz,w)
print(formatowanie)

owoce = [
      ('awokado',7.88),
      ('banan',4.99),
      ('jabłko',3.41),
      ('mandarynka',9.99),
      ('malina',12.11)
]

#stwórz cennik wg wzoru (linia cennika) -> #nr: nazwa(10) = 0.00 zł
print("__________________________________________")
for i,(nazwa,cena) in enumerate(owoce):
      print('#%d: %-10s = %6.2f zł' %(i,nazwa,cena))

print("__________________________________________")
for i,(nazwa,cena) in enumerate(owoce):
      print('#%d: %-10s = %6.2f zł' %(
            i+1,
            nazwa.title(),
            round(cena,1)
      ))
