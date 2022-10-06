from functools import partial

def policz(a,b):
    return (a+1)**(b-1)

#funkcje częściowe - partial function

pl2 = partial(policz,b=2)
pl4 = partial(policz,b=4)
policz_5 = partial(policz,5)

print("______________________")
print(policz(3,6))
print("______________________")
print(pl2(2))
print("______________________")
print(pl4(2))
print("______________________")
print(policz_5(2))
