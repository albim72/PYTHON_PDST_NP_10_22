#funkcja kwota(transport,nocleg_wyz,wycieczki,ubezp,inne,rabat) ->
#(transport + nocleg_wyz)*(1-rabat/100)+wycieczki+ubezp+inne

#pozwalaj tylko na wprowadzenie rabatu z zakresu (1-70%)
#blokuj roziwązanie dla innych wartości
#wartość 0 dla rabatu uczyńmy wartością domyślną parametru rabat (rabat=0)
