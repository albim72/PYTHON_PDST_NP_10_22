import itertools

#przykład 1
for i in itertools.count(5,5):
    if i==35:
        break
    else:
        print(i,end=" ")

#przykład 2 > cykle
print()
print("______________________________________")
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

        
        #przykład 3

fitness = ['trening','siła','regenracja','dieta','zawody']
iterators = itertools.cycle(fitness)
print()
print("______________________________________")
for i in range(18):
    print(next(iterators), end=" ")

    
 #przyklad 4

from itertools import product

print("iloczyn kartezjański z użyciem repeat:")
print(list(product([1,2], repeat=2)))
print()

print("iloczyn kartezjański przez container:")
print(list(product(fitness,'2')))
print()

print("iloczyn kartezjański przez container:")
print(list(product(fitness,[2,3,5])))
print()
