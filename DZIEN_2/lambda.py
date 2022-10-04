print((lambda x:x**2)(34))

x = lambda a:a+113
print(x(9))

def policz(a):
    return a+113

print(policz(9))

y = lambda a,b,c=2:(a-c)*b

print(y(4,7,9))
print(y(4,7))

def multi(n):
    return lambda a:a*n

h = multi(6)
print(h(8))
print(multi(12)(5))

nb = [56,12,3,7,9,14,20,2,4,5,101,99,90,40]

#zadanie1 -> stwórz nową listę parzyste i przkaż do niej wszytkie wartości parzyste z listy nb
#filter(funkcja z warunkami,dane)

parzyste = list(filter(lambda x:x%2==0,nb))
print(parzyste)

#zadanie2 - > stwórz nową listę cube i przekaż (zamapuj) do niej wartości z listy nb podniesione każda do potęgi trzeciej

cube = list(map(lambda x:x**3,nb))
print(cube)
