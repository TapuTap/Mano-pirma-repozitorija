# Trečia užduotis
# Atidarykite "tekstas.txt" failą, pakeiskite failo žymeklį 
# į vidurį failo ir atspausdinkite likusį failo turinį.
with open("darbas_su_failais/tekstas.txt", "r") as failas:
    turinys = failas.read()
    teksto_vidurys = len(turinys) // 2
    failas.seek(teksto_vidurys)
    teksto_dalis = failas.read()
    print(teksto_dalis)
