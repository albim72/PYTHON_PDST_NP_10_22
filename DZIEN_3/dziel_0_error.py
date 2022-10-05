def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("brak dostępnej wartości...")
    except TypeError:
        print("możesz dzielić tylko liczby!")
    except:
        print("coś poszło nie tak....")
    else:
        print(f"wynik dzielenia x/y = {wynik}")
    finally:
        print("policzmy coś jeszcze!")

try:
    dzielenie(6,7)
    dzielenie(6,0)
    dzielenie(0,0)
    dzielenie(0.9987,101.0988)
    dzielenie(6,True)
    dzielenie(6,False)
    dzielenie(107E332,45)
    dzielenie("gfdfdfgd",6)
    dzielenie(4)
except TypeError:
    print("podaj właścią liczbę argumentów funkcji dzielenie(x,y)")
