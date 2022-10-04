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
