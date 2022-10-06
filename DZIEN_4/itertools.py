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
