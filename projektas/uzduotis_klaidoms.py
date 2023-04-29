while True:
    try:
        skaicius = float(input("Įveskite teigiamą skaičių"))
        if skaicius < 0:
            raise ValueError("Įvestas skaičius yra neigiamas")
        else:
            print("Ačiū, jūs įvedėte:", skaicius)
            break
    except ValueError as error:
        print("Klaida:", error)