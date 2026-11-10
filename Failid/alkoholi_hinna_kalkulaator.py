import sys
import subprocess

# Kontrollib kas vajalik graphics library on olemas
# Kui pole, paigaldab programm selle automaatselt taustal.
try:
    import FreeSimpleGUI as sg
except ModuleNotFoundError:
    print("Paigaldan vajaliku teegi (FreeSimpleGUI)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "FreeSimpleGUI"])
    import FreeSimpleGUI as sg

# Küsib kasutajalt, mitut erinevat jooki soovitakse võrrelda
vastus = sg.popup_get_text("Mitu erinevat alkoholi on?")

if vastus != None and vastus != "":
    mitu = int(vastus)

    # Järjendid arvutatud tulemuste meelespidamiseks
    joogid = []
    hinnad = []

    # Käime labi koik joogid ja küsime nende andmed
    for i in range(1, mitu + 1):
        kogus = float(sg.popup_get_text("Kui palju on alkoholi " + str(i) + " (ml)?"))
        kraad = float(sg.popup_get_text("Mitu kraadi on alkohol " + str(i) + " (%):"))
        hind = float(sg.popup_get_text("Kui palju see kogus maksab (€)?"))

        # Arvutame puhta alkoholi koguse (ml) ja selle yhe milliliitri hinna
        puhas = kogus * kraad / 100
        hind_ml = hind / puhas

        # Lisame tulemused nimekirjadesse
        joogid.append(puhas)
        hinnad.append(hind_ml)

    # Paneme kokku teksti, mida lõppaknas kuvada
    valjund = ""

    for i in range(mitu):
        valjund += "Alkohol " + str(i + 1) + "\n"
        valjund += "Puhast alkoholi: " + str(joogid[i]) + " ml\n"
        valjund += "1 ml puhta alkoholi hind: " + str(round(hinnad[i], 4)) + " €\n\n"

    # Leiame kõige madalama 1 ml hinna ja selle joogi järjekorranumbri
    soodsaim = min(hinnad)
    number = hinnad.index(soodsaim) + 1

    valjund += "Hinna suhtes on soodsam alkohol " + str(number)

    # Kuvame tulemused eraldi teateaknas
    sg.popup("Tulemused", valjund)
