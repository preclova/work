# narysuj tabliczkę mnożenia
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16
# itd.
# postaraj się ładnie to wyświetlać
# użyj znaku "\t" do wyświetlania tabulatora

for x in range(1, 11) :
# print(x)
    for y in range(1, 11) :
        print("\t", x * y, end= '')



