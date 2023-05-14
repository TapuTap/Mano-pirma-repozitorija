-- SQLite
-- CREATE TABLE klientai (
-- id INTEGER PRIMARY KEY AUTOINCREMENT,
-- vardas VARCHAR(50),
-- pavardė VARCHAR(50),
-- adresas VARCHAR(100),
-- el_paštas VARCHAR(50)
-- );
-- ALTER TABLE klientai
-- ADD telefonas VARCHAR(20);

-- Pirma užduotis
-- Sukurkite lentelę pavadinimu "studentai", kuri turės šiuos 
-- stulpelius:
-- studento_id: sveikas skaičius, PRIMARY KEY
-- vardas: tekstas, maksimalus ilgis - 50 simbolių
-- pavardė: tekstas, maksimalus ilgis - 50 simbolių
-- studijų_programa: tekstas, maksimalus ilgis - 100 simbolių
-- el_paštas: tekstas, maksimalus ilgis - 50 simbolių
-- Modifikuokite lentelę "studentai" - prie "studentai" 
-- lentelės pridėkite naują stulpelį "gimimo_data" su datos tipu.
-- Pakeiskite "studijų_programa" stulpelio tipą į TEXT.
-- Pašalinkite lentelę "studentai"
-- Pašalinkite "studentai" lentelę iš duomenų bazės.
CREATE TABLE studentai (
id INTEGER PRIMARY KEY AUTOINCREMENT,
vardas VARCHAR(50),
pavarde VARCHAR(50),
studiju_programa VARCHAR(100),
el_pastas VARCHAR(50)
);

ALTER TABLE studentai
ADD gimimo_data DATE;


DROP TABLE studentai;

-- Antra užduotis
-- Sukurkite lentelę "dėstytojai", kuri turės šiuos stulpelius:
-- vardas: tekstas, maksimalus ilgis - 50 simbolių
-- pavardė: tekstas, maksimalus ilgis - 50 simbolių
-- skyrius: tekstas, maksimalus ilgis - 100 simbolių
-- el_paštas: tekstas, maksimalus ilgis - 50 simbolių
-- Prie "dėstytojai" lentelės pridėkite naują stulpelį
--  "kabineto_nr" su sveiko skaičiaus tipu.

-- Pašalinkite "dėstytojai" lentelę iš duomenų bazės.
CREATE TABLE dėstytojai (
vardas VARCHAR(50),
pavarde VARCHAR(50),
skyrius VARCHAR(100),
el_pastas VARCHAR(50)
);

ALTER TABLE dėstytojai
ADD kabineto_nr INTEGER;

DROP TABLE dėstytojai
