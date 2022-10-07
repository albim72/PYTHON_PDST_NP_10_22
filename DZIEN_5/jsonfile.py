import json

json_str = '{"imiona":["Jan","Leon"],"nazwisko":"Kot","data_urodzenia":"1974-10-09","liczba_punktow":45}'

print(json_str)
print(type(json_str))

# d = dict(json_str)
# print(d)
#błąd konwersji!

json_d = json.loads(json_str)

print(json_d)
print(type(json_d))

print(json_d["liczba_punktow"])

print(f"pierwsze imię: {json_d['imiona'][0]}, nazwisko: {json_d['nazwisko']}")

sam = {
    "marka":"Opel",
    "model":"Insignia",
    "rocznik":2020,
    "poj":2.2
}

jsonauto = json.dumps(sam,indent=4)

print(jsonauto)
print(type(jsonauto))

with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("samochod.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
print(auto_dict["marka"])

