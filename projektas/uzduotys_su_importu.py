# Pirma užduotis
# Parašykite funkciją, kuris atspausdina 10 atsitiktinių skaičių 
# nuo 1 iki 100 ir juos išrikiuoja didėjimo tvarka.
# import random

# def rusiuoti_atsitiktinius_skaicius():
#     skaiciu_sarasas = []
#     while len(skaiciu_sarasas) < 10:
#         skaicius = random.randint(1, 100)
#         skaiciu_sarasas.append(skaicius)
#     rikiuoti_skaiciai = sorted(skaiciu_sarasas)
#     print(rikiuoti_skaiciai)

# rusiuoti_atsitiktinius_skaicius()

# Antra užduotis
# Sukurkite kauliukų žaidimą, kuris:

# Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
# Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
# Kitu atveju atspausdinti „Laimėjai!“
# Patarimas: Naudoti ciklą

# import random

# print('Bus sugeneruoti 3 skaičiai')
# print('Jei vienas iš jų – 5, tu pralaimėjai!')

# for bandymas in range(3):
#     skaicius = random.randint(1, 6)
#     print(skaicius)
#     if skaicius == 5:
#         print('Pralaimėjai...')
#         break
# else:
#     print('Laimėjai!')

# Trečia užduotis
# Parašykite Python funkciją, kuri priima metus ir mėnesį, 
# o tada atspausdina šio mėnesio kalendorių bei parodo, 
# kiek savaitgalio dienų (šeštadienių ir sekmadienių) yra tame mėnesyje.
# import calendar
# def spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(metai, menesis):
#     print(calendar.month(metai, menesis))
#     _, menesio_ilgis = calendar.monthrange(metai, menesis)

#     savaitgalio_dienos = 0
#     for diena in range(1, menesio_ilgis + 1):
#         savaites_diena = calendar.weekday(metai, menesis, diena)
#         if savaites_diena == 5 or savaites_diena == 6:
#             savaitgalio_dienos += 1

#     print(f"Savaitgalio dienų skaičius šiame mėnesyje: {savaitgalio_dienos}")

# # Pavyzdys su 2023-ųjų balandžio mėnesiu
# spausdinti_menesio_kalendoriu_suskaiciuojant_savaitgalius(2023, 4)





# Pirma užduotis
# Parašykite programą, kuri pateiktų dabartinį laiką,
# bet tik minutes ir sekundes.
# from datetime import datetime
# siandien = datetime.now()
# kaip_formatuoti = "%M:%S"
# konvertuotas_laikas = siandien.strftime(kaip_formatuoti)
# print(konvertuotas_laikas)


# Antra užduotis
# Sukurkite funkciją, kuri priimtų gimimo datą kaip
# stringą (formatu "%Y-%m-%d") ir grąžintų, kiek dienų liko 
# iki jūsų gimtadienio

# from datetime import datetime, timedelta

# def dienos_iki_gimtadienio(gimimo_data):
#     gimimo_data_format = datetime.strptime(gimimo_data, "%Y-%m-%d")
#     siandiena = datetime.now()
#     gimtadienio_data = gimimo_data_format.replace(year=siandiena.year)

#     if gimtadienio_data < siandiena:
#         gimtadienio_data = gimtadienio_data.replace(year=siandiena.year + 1)

#     skirtumas = gimtadienio_data - siandiena
#     return skirtumas.days

# gimimo_data = "1992-09-07"
# print(f"Liko {dienos_iki_gimtadienio(gimimo_data)} dienos (-ų) iki gimtadienio.")



# Trečia užduotis
# Parašykite programą, kuri priimtų datą ir laiką stringo 
# formatu (pavyzdžiui, "2023-05-21 15:30"), pridėtų prie to
# 48 valandas ir grąžintų naują datą ir laiką stringo formatu.
# 
# from datetime import datetime, timedelta

# def prideti_48_valandas(data_laikas):
#     format_string = "%Y-%m-%d %H:%M"
#     date_object = datetime.strptime(data_laikas, format_string)
#     naujas_date_object = date_object + timedelta(hours=48)
#     naujas_data_laikas = naujas_date_object.strftime(format_string)
#     return naujas_data_laikas

# data_laikas = "2023-05-21 15:30"
# print(f"Pridėjus 48 valandas: {prideti_48_valandas(data_laikas)}")





# Ketvirta užduotis
# Parašykite programą, kuri priimtų du laikotarpius kaip 
# timestamp'us ir grąžintų laikotarpių skirtumą dienomis.
# from datetime import datetime

# def skirtumas_dienomis(timestamp1, timestamp2):
#     date_object1 = datetime.fromtimestamp(timestamp1)
#     date_object2 = datetime.fromtimestamp(timestamp2)
#     skirtumas = abs(date_object2 - date_object1)
#     return skirtumas.days

# timestamp1 = 1671395400
# timestamp2 = 1674000000
# print(f"Laikotarpių skirtumas dienomis: {skirtumas_dienomis(timestamp1, timestamp2)}")





# 💡 Penkta užduotis
# Sukurkite funkciją, kuri priimtų datą kaip stringą
# (pavyzdžiui, "2023-06-01") ir grąžintų,
# kokia savaitės diena yra ta data
# (pavyzdžiui, "Pirmadienis", "Antradienis" ir tt.).



# from datetime import datetime

# def savaites_diena(data):
#     format_string = "%Y-%m-%d"
#     date_object = datetime.strptime(data, format_string)
#     dienos = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis", "Šeštadienis", "Sekmadienis"]
#     return dienos[date_object.weekday()]

# data = "2023-06-01"
# print(f"Ši data yra {savaites_diena(data)}")

# from zoneinfo import ZoneInfo
# from datetime import datetime

# # Sukurti "aware" datetime objektą su nurodyta laiko zona
# laikas = datetime(2023, 4, 12, 18, 30, tzinfo=ZoneInfo("Europe/Vilnius"))
# print(laikas)
# from zoneinfo import available_timezones

# for time_zone in available_timezones():
    # print(time_zone)





# Parašykite programą, kuri išvestų sąrašą visų laiko zonų, 
# kurių pavadinime yra "America".

# from zoneinfo import available_timezones

# america_time_zones = []

# for tz in available_timezones():
#     if "America" in tz:
#         america_time_zones.append(tz)

# for time_zone in america_time_zones:
#     print(time_zone)

