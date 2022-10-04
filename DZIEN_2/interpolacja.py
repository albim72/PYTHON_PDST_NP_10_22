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
