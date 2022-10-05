def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0!")
    except NameError:
        print("brak dostępnej wartości...")
    except:
        print("coś poszło nie tak....")
    else:
        print(f"wynik dzielenia x/y = {wynik}")
    finally:
        print("policzmy coś jeszcze!")

dzielenie(6,7)
dzielenie(6,0)
dzielenie(0,0)
dzielenie(0.9987,101.0988)
dzielenie(6,True)
dzielenie(6,False)
dzielenie(107E332,45)
