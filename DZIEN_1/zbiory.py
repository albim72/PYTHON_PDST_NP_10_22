drzewa = {"sosna","dąb","buk","jesion","baobab","jabłoń","klon"}
print(drzewa)
print(drzewa)
print(drzewa)

print("____________________________________")
for d in drzewa:
    print(d)
print("____________________________________")

print("osika" in drzewa)
drzewa.add("osika")

print(drzewa)
las = ["brzoza","jodła","buk","świerk","jałowiec"]
drzewa.update(las)
print(drzewa)

drzewa.remove("jodła")
print(drzewa)

drzewa.discard("akacja")
print(drzewa)

drzewa.discard("klon")
print(drzewa)

dm = drzewa.pop()
print(dm)

print(drzewa)
