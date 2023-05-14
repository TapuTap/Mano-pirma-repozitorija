-- Pirma užduotis
-- Sukurkite lentelę "mokytojai" su šiais stulpeliais: 
-- "id", "vardas", "pavarde", "specialybe" ir "patirtis_metais".

CREATE TABLE mokytojai(
id INT PRIMARY KEY,
vardas VARCHAR(50) NOT NULL,
pavarde VARCHAR(50) NOT NULL,
specialybe VARCHAR(100),
patiris_metais INTEGER
);

-- Antra užduotis
-- Įterpkite šiuos įrašus į sukurtą lentelę "mokytojai":

-- Mokytojas su ID 1, vardu Petras, pavarde Petraitis, 
-- specialybe Matematika ir dirba nuo 2013 metų.

-- Mokytojas su ID 2, vardu Ona, pavarde Onaitė, 
-- specialybe Fizika ir dirba nuo 2012 metų.

-- Mokytojas su ID 3, vardu Marius, pavarde Marijus, 
-- specialybe Biologija ir dirba nuo 2015 metų.

-- Mokytojas su ID 4, vardu Rasa, pavarde Rasaitė,
--  specialybe Anglų kalba ir dirba nuo 2011 metų.

-- Mokytojas su ID 5, vardu Aurimas, pavarde Aurimaitis,
--  specialybe Lietuvių kalba ir dirba nuo 2018 metų.

-- Mokytojas su ID 6, vardu Gintare, pavarde Gintarėlė, 
-- specialybe Istorija ir dirba nuo 2020 metų.

INSERT INTO mokytojai(id, vardas, pavarde, specialybe, patiris_metais)
VALUES
(1, "Petras", "Petraitis", "Matematika", 2013),
(2, "Ona", "Onaitė", "Fizika", 2012),
(3, "Marius", "Marijus", "Biologija", 2015),
(4, "Rasa", "Rasaitė", "Anglų kalba", 2011),
(5, "Aurimas", "Aurimaitis", "Lietuvių kalba", 2018),
(6, "Gintarė", "Gintarėlė", "Istorija", 2020);

-- Trečia užduotis
-- Parodykite visus įrašus iš lentelės "mokytojai", 
-- kurių specialybė yra "Matematika".
SELECT * FROM mokytojai WHERE specialybe = "Matematika";

-- Ketvirta užduotis
-- Raskite visus mokytojus, kurių stažas yra ilgesnis nei 8 arba 9 metai, 
-- ir atvaizduokite tik jų vardą, pavardę bei specialybę.
SELECT vardas, pavarde, specialybe FROM mokytojai
WHERE (2023 - patiris_metais) > 8 or (2023 - patiris_metais) > 9;

-- Penkta užduotis
-- Pakeiskite mokytojos, vardu Rasa ir pavarde Rasaitė, pavardę į "Žolienė".
UPDATE mokytojai SET pavarde = "Žolienė" WHERE pavarde = "Rasaitė"

-- Šešta užduotis
-- Ištrinkite iš lentelės "mokytojai" mokytoją, kurio ID yra 4.

DELETE FROM mokytojai WHERE id = 4;

