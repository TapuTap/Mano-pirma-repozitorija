# amžius = 29
# if amžius > 0:
#     print("Skaičius yra teigiamas")
# else:
#     print ("Skaičius yra neigiamas")


# amžius = 30
# if amžius >= 5 and amžius <= 10:
#     print("Skaičius yra tarp 5 ir 10")
# else:
#     print("Skaičius nėra tarp 5 ir 10")


# a = 15
# b = 25
# if a > 0 and b > 0:
#     print("Abu skaičiai didesni nei 0")
# else:
#     print("Bent vienas skaičius yra neigiamas arba lygus 0")

# a = 15
# b = 25

# if a % 2 == 0 or b % 2 == 0:
#     print("Bent vienas skaičius yra lyginis")
# else:
#     print("Abu skaičiai yra nelyginiai")



# kintamasis = input("Įveskite simbolių eilutę: ")
# print("Pirmasis simbolis:", kintamasis[0])
# print("Paskutinis simbolis:", kintamasis[-1])

# knygos_pavadinimas = "ACOTAR"
# print(knygos_pavadinimas[:5])

# citata = "Tik negyvos žuvis plaukia pasroviui"
# print(citata[-3:])

# pirmas_zodis = input("Įveskite pirmąjį žodį: ")
# antras_zodis = input("Įveskite antrąjį žodį: ")
# print(pirmas_zodis[0] + "-" + antras_zodis[0])







# vardas = input("Įveskite savo vardą: ")
# metai = input("Įveskite savo amžių: ")
# metai_iki_100 = 100 - int(metai)
# rezultatas = 2023 + metai_iki_100
# print(f"Sveiki, {vardas}! Jūms sukaks 100 metų {rezultatas}-aisiais.")



# ugis_cm = input("Įveskite savo ūgį centimetrais: ")
# ugis_m = int(ugis_cm) / 100
# print(f"Jūsų ūgis yra {ugis_cm} cm arba {ugis_m:.2f} m.")


# atlyginimas = input("Įveskite savo atlyginimą: ")
# mokescio_procentas = input("Įveskite taikomą mokesčio procentą: ")
# neto_atlyginimas = int(atlyginimas) * (1 - int(mokescio_procentas) / 100)
# print(f"Jūsų atlyginimas į rankas yra: {neto_atlyginimas:.2f} EUR")

konversijos_tipas = input("Pasirinkite konversijos tipą (įveskite C arba F): ")
temperatura = input("Įveskite temperatūrą: ")

if konversijos_tipas == "C":
    fahrenheit = float(temperatura) * 9/5 + 32
    print(f"{temperatura} laipsnių Celsijaus yra {fahrenheit:.2f} laipsnių Farenheito.")
elif konversijos_tipas == "F":
    celsius = (float(temperatura) - 32) * 5/9
    print(f"{temperatura} laipsnių Farenheito yra {celsius:.2f} laipsnių Celsijaus.")
else:
    print("Neteisingas konversijos tipas. Bandykite dar kartą.")