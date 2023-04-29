# Pirma užduotis
# Atidarykite tekstiniame faile esančią eilutę ir atspausdinkite ją,
# pakeičiant visus didžiąsias raides mažosiomis ir atvirkščiai. 
# Failo pavadinimas: "pakeitimai.txt".💡
# Galite naudoti swapcase() funkciją.

with open("darbas_su_failais/pakeitimai.txt", "r", encoding="utf-8") as failas:
    pakeistos_raides = failas.read().swapcase()
    print(pakeistos_raides)
