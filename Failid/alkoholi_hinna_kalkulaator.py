import sys
import subprocess

try:
    import FreeSimpleGUI as sg
except ModuleNotFoundError:
    print("Paigaldan vajaliku teegi (FreeSimpleGUI)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "FreeSimpleGUI"])
    import FreeSimpleGUI as sg
vastus = sg.popup_get_text("Mitu erinevat alkoholi on?")

if vastus != None and vastus != "":
    mitu = int(vastus)

    joogid = []
    hinnad = []

    for i in range(1, mitu + 1):
        kogus = float(sg.popup_get_text("Kui palju on alkoholi " + str(i) + " (ml)?"))
        kraad = float(sg.popup_get_text("Mitu kraadi on alkohol " + str(i) + " (%):"))
        hind = float(sg.popup_get_text("Kui palju see kogus maksab (€)?"))

        puhas = kogus * kraad / 100
        hind_ml = hind / puhas

        joogid.append(puhas)
        hinnad.append(hind_ml)

    valjund = ""

    for i in range(mitu):
        valjund += "Alkohol " + str(i + 1) + "\n"
        valjund += "Puhast alkoholi: " + str(joogid[i]) + " ml\n"
        valjund += "1 ml puhta alkoholi hind: " + str(round(hinnad[i], 4)) + " €\n\n"

    soodsaim = min(hinnad)
    number = hinnad.index(soodsaim) + 1

    valjund += "Hinna suhtes on soodsam alkohol " + str(number)

    sg.popup("Tulemused", valjund)
