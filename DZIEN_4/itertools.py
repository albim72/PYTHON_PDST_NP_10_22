import itertools

#przykład 1
for i in itertools.count(5,5):
    if i==35:
        break
    else:
        print(i,end=" ")
