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
