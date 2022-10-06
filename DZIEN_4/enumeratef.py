zakupy = ['chleb','masło','śledź','jogurt naturalny']

for i in zakupy:
    print(i)

print("_____________________________")

for item in enumerate(zakupy):
    print(item)
print("_____________________________")
for (i,wart) in enumerate(zakupy,1012):
    print(f"id:{i} -> {wart}")
