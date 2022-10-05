def policz(x,y,z):
    return x**2+y**2+z**2
try:
    print(policz(3,6,7))
    print(policz(2.2,8.9,7))
    print(policz(0.00056,222,12E+56))

    print(policz(1,1,True))
    print(policz(1,1))

except TypeError:
    print("wprowadż trzy parametry do funkcji policz(x,y,z)")

print(policz(5,6,8))

#przekształć program w ten sposób żeby aktualnej sytuacji nie przzerywał programu z kodem 1
#tylko wyświetlał komunikat: wprowadż trzy parametry do funkcji policz(x,y,z)
#ostatecznie wyjście z programu z kodem 0

