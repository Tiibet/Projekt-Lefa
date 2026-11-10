mitu = int(input("Mitu erinevat alkoholi on? "))

joogid = []
hinnad_ml = []

for i in range(1, mitu + 1):
    kogus = float(input("Kui palju on alkoholi " + str(i) + " (ml)? "))
    kraad = float(input("Mitu kraadi on alkohol " + str(i) + " (%): "))
    hind = float(input("Kui palju see kogus maksab (€)? "))

    puhas = kogus * kraad / 100
    hind_ml = hind / puhas

    joogid.append(puhas)
    hinnad_ml.append(hind_ml)

print()

for i in range(mitu):
    print("Alkohol", i + 1)
    print("Puhast alkoholi:", joogid[i], "ml")
    print("1 ml puhta alkoholi hind:", round(hinnad_ml[i], 4), "€")
    print()

soodsaim = min(hinnad_ml)
soodsaima_number = hinnad_ml.index(soodsaim) + 1

print("Hinna suhtes on soodsam alkohol", soodsaima_number)