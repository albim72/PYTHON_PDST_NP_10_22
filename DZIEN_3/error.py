try:
    x = 8
    print(x)
except NameError:
    print("x nie istnieje!")
except:
    print("nieokreślony błąd")
finally:
    y = 45
    print(f"y = {y}")

print("ciąg dalszy")
