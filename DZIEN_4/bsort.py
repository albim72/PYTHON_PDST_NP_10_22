nazwa_classic = ['samolot','miecz','mecz','Mieczysław','romb','Roman','marchewka',
                 'zenit','piorun','macierz','123']

def pomniejsz_tab(t):
    for i,w in enumerate(t):
        t[i] = w.lower()
    return t

def bsort_classic(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i] < a[i-1]:
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

bsort_classic(pomniejsz_tab(nazwa_classic))
print(nazwa_classic)
