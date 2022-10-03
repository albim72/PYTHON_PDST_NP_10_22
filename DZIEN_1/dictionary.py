#słownik -> struktura asocjacyjna (klucz,wartość)

samochod = {
    "marka":"Ford",
    "model":"Mustang",
    "rocznik":1974
}

print(samochod)
print(samochod["marka"])
samochod["rocznik"] = 2020

print(samochod)

samochod["poj"] = 4.2
print(samochod)

print(samochod.items())
print(samochod.keys())
print(samochod.values())

print("________________lista kluczy_______________________________")

for x in samochod:
    print(x)
print("________________lista wartości_______________________________")

for y in samochod:
    print(samochod[y])

print("________________lista wartości_______________________________")

for g in samochod.values():
    print(g)

print("________________lista itemów_______________________________")

for x,y in samochod.items():
    print(x,":",y)

autokomis = {
    "auto1":{
        "marka":"Ford",
        "model":"Mustang",
        "rocznik":1974
        },
    "auto2":{
        "marka":"Opel",
        "model":"Vectra",
        "rocznik":2008
        },
    "auto3":{
        "marka":"Jeep",
        "model":"Cherokee",
        "rocznik":2019
        }

}

print(autokomis)

for a in autokomis.values():
    print(a)


print(autokomis["auto2"]["marka"])
