# powkładaj z listy wartości do odpowiednich "worków"

import random

owoce = ["jablko"] * 4 + ["pomarancz"] * 3 + ["mandarynka"] * 4 + \
    ["gruszka"] * 3 + ["pomidor"] * 4

jablka = []
pomarancze = []
mandarynki = []
gruszki = []
pomidory = []

random.shuffle(owoce)
print(owoce)

for element in owoce: 
    if element == "jablko":
       jablka.append(element)
    elif element == "pomarancz":
       pomarancze.append(element)
    elif element == "mandarynka":
        mandarynki.append(element)
    elif element == "gruszka":
        gruszki.append(element)
    elif element == "pomidor":
        pomidory.append(element)
print(pomarancze)
