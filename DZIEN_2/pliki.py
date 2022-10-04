import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

f.close()

print("**********************************")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("**********************************")
f = open("dane.txt","r",encoding="utf-8")
for w in f:
    print(w)
f.close()

f = open("message.txt","a",encoding="utf-8")
f.write("to jest linia tesktu w pliku\n")
f.close()

f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje")
