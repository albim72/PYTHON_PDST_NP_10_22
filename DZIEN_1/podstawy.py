print("to jest pierwsza linia programu!")

a = 45

print(a)
print(type(a))

a = "wartość tekstowa"
print(a)
print(type(a))

b:float
b=8.458
print(b)
print(type(b))

b = True
print(b)
print(type(b))

s1 = "pora roku: jesień"
s2 = "następna pora: zima"
r = 2022

#komentarz -> symbol + konkatenacja (łączenie) ciągów string
print(s1+ ", " + s2 + ", " + str(r))

print(s1,s2,r,sep=", ")

y = 13.66719
print(14*y)

x = "17.98"
print(14*x)
print(14*float(x))
#CTRL+D -> powielenie linii lub bloku
print(14*eval(x))

g1 = 10
g2 = 11

print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2)

d = 3.786543
print(round(d))
print(round(d,1))
print(round(d,2))

print(pow(4,5))
print(4**5)

import math

print(6*math.exp(4))

u = 1
u+=1
print(u)
