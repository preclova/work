wynik = 75

# 1. sprawdzenie jaka jest ocena
if wynik >= 91:
    ocena = 5.0
elif wynik >= 81:
    ocena = 4.5
elif wynik >= 71:
    ocena = 4.0
elif wynik >= 61:
    ocena = 3.5
elif wynik >= 50:
    ocena = 3.0
else:
    ocena = 2.0

# 2. wyświetlenie tekstu
if ocena == 2.0:
    print("Postaraj się bardziej następnym razem")
elif ocena == 3.0:
    print("Ledwo zdałeś")
elif ocena == 3.5:
    print("Jeszcze trochę pracy przed tobą")
elif ocena == 4.0:
    print("Dobrze!")
elif ocena == 4.5:
    print("Masz prawie najlepszy wynik, tak trzymaj!")
else:
    print("Gratulacje! Najlepsza ocena!")
    