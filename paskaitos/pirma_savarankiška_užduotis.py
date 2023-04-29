# Valiutos konvertuoklis su 2 valiutomis

# valiutos_tipas = input ("Pasirinkite valiutą (Įveskite EUR arba USD): ")
# pinigų_suma = input("Įveskite pinigų sumą: ")
# dolerio_kursas_vs_eur = 1.094
# euro_kursas_vs_doleris = 0.879

# if valiutos_tipas == "EUR":
#     doleriai = float(pinigų_suma) * dolerio_kursas_vs_eur
#     print(f"{pinigų_suma} EUR yra {doleriai:.03f} USD")
# elif valiutos_tipas == "USD":
#     eurai = float(pinigų_suma) * euro_kursas_vs_doleris
#     print(f"{pinigų_suma} USD yra {eurai:.03f} EUR")
# else:
#     print("Neteisingai įvedėte valiutos tipą")


#Valiutos konvertuoklis su 3 valiutomis

valiutos_tipas1 = input ("Pasirinkite valiutą (Įveskite EUR, USD arba GBP): ")
valiutos_tipa2 = input ("Pasirinkite valiutą (Įveskite EUR,USD arba GBP): ")
pinigų_suma = input("Įveskite pinigų sumą: ")
dolerio_kursas_vs_eur = 0.879
euro_kursas_vs_doleris = 1.094
svaro_kursas_vs_eur = 1.098
euro_kursas_vs_svaras = 0.873
svaro_kursas_vs_doleris = 1.201
dolerio_kursas_vs_svaras = 0.767

if valiutos_tipas1 == "EUR" and valiutos_tipa2 == "USD":
    doleriai_iš_eurų = float(pinigų_suma) * euro_kursas_vs_doleris
    print(f"{pinigų_suma} EUR yra {doleriai_iš_eurų:.03f} USD")

elif valiutos_tipas1 == "EUR" and valiutos_tipa2 == "GBP":
    svarai_iš_eurų = float(pinigų_suma) * euro_kursas_vs_svaras
    print(f"{pinigų_suma} EUR yra {svarai_iš_eurų:.03f} USD")

elif valiutos_tipas1 == "USD" and valiutos_tipa2 == "EUR":
    eurai_iš_dolerių = float(pinigų_suma) * dolerio_kursas_vs_eur
    print(f"{pinigų_suma} USD yra {eurai_iš_dolerių:.03f} EUR")

elif valiutos_tipas1 == "USD" and valiutos_tipa2 == "GBP":
    svarai_iš_dolerių = float(pinigų_suma) * dolerio_kursas_vs_svaras
    print(f"{pinigų_suma} USD yra {svarai_iš_dolerių:.03f} EUR")

elif valiutos_tipas1 == "GBP" and valiutos_tipa2 == "EUR":
    eurai_iš_svarų = float(pinigų_suma) * svaro_kursas_vs_eur
    print(f"{pinigų_suma} USD yra {eurai_iš_svarų:.03f} EUR")

elif valiutos_tipas1 == "GBP" and valiutos_tipa2 == "USD":
    doleriai_iš_svarų = float(pinigų_suma) * svaro_kursas_vs_doleris
    print(f"{pinigų_suma} USD yra {doleriai_iš_svarų:.03f} EUR")

else:
    print("Neteisingai įvedėte valiutos tipą")

#Reikia padaryti valiutos konvertuoklį pririšant visas valiutas prie vienos valiutos














