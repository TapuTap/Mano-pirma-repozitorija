# Antra užduotis
# Sukurkite naują failą "skaiciai.txt" ir įrašykite
# į jį skaičius nuo 1 iki 100, kiekvieną naujoje eilutėje.
with open("darbas_su_failais/skaiciai.txt", "w") as failas:
    for skaiciai in range(1,101):
        failas.write(str(skaiciai) + "\n")