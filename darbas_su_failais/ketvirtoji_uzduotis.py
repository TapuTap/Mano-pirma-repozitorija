# Ketvirta užduotis
# Sukurkite failą "eilutes.txt" ir įrašykite į jį šias eilutes:
# Saulėlydis žėri žemę švelniai.
# Vakare vėjas šnypščia medžius.
# Vėjas nerimsta, šnypščia ir švilpia.
# Papildykite failą "eilutes.txt" nauja eilute,
# kuri yra jūsų vardas ir pavardė.

# Atidarykite "eilutes.txt" failą, perskaitykite jo turinį ir 
# atspausdinkite visas eilutes, kuriose yra žodis "vėjas".

with open("darbas_su_failais/eilutes.txt", "w+", encoding="utf-8") as failas:
    eilutes = ("Saulėlydis žėri žemę švelniai.\n", "Vakare vėjas šnypščia medžius.\n" , "Vėjas nerimsta, šnypščia ir švilpia.\n")
    failas.writelines(eilutes)
with open("darbas_su_failais/eilutes.txt", "a", encoding="utf-8") as failas:
    failas.writelines("Raimonda Anisimova.\n")
    failas.seek(0)  # grįžkite į failo pradžią
with open("darbas_su_failais/eilutes.txt", "r", encoding="utf-8") as failas:
    turinys = failas.read()
    print("Naujas turinys:", turinys)
with open("darbas_su_failais/eilutes.txt", "r", encoding="utf-8") as failas:
    for eilute in failas:
        if "vėjas" in eilute:
            print(eilute)