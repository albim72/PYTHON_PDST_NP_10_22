mecz = "MECZ MIESIĄCA:\nklub sportowy: \"Orły Wisła\"-\ttrener: Jan Kot\nlokalizacja: Janowo\n" \
       "vs\nklub sportowy: \"KS Piotków\"-\ttrener: Adam Nowak\nlokalizacja: Piotrków\n"
print(mecz)

str_ = "        niezwykle ważna i Tajna wiadomość;     FT785698694;      i Tajna pRZesYłKA"

print(str_.upper())
print(str_.lower())
print(str_.strip())
print(str_.replace("Tajna","Utajniona"))
print(str_.split(";"))


ltxt = list(str_.split(";"))
print(ltxt)

for i,ltxt_wart in enumerate(ltxt):
       ltxt[i] = ltxt_wart.strip()

print(ltxt)

print(str_.find("Tajna"))
print(str_.endswith("ka"))
print(str_.endswith("KA"))

d = "pionierzy"
e = "12222222"

print(d.isalpha())
print(e.isdigit())
