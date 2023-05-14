-- SQLite
-- Pirma užduotis
-- Sukurkite duomenų bazę, kurioje saugosite informaciją 
-- apie studentų duomenis ir jų kursus. Kiekvienas studentas
--  gali mokytis daugelyje kursų, ir kiekvienas kursas gali
--   turėti daug studentų. Sukurkite atitinkamas lentelės 
--   ir susiekite jas Many-to-Many ryšiu.

CREATE TABLE Studentai (
id INTEGER PRIMARY KEY AUTOINCREMENT,
vardas VARCHAR(50),
pavarde VARCHAR(50),
el_pastas VARCHAR(100),
telefonas VARCHAR(20)
);

CREATE TABLE Kursai (
id INTEGER PRIMARY KEY,
pavadinimas VARCHAR(50),
aprasymas TEXT(4000)
);

CREATE TABLE Studentukursai (
id INTEGER PRIMARY KEY,
studentai_id INTEGER REFERENCES Studentai(id),
kursai_id INTEGER REFERENCES Kursai(id)
);

-- Antra užduotis
-- Sukurkite duomenų bazę, kurioje saugosite informaciją 
-- apie prekes ir jų kategorijas. Kiekviena prekė gali 
-- priklausyti tik vienai kategorijai, tačiau kiekviena 
-- kategorija gali turėti daug prekių. Sukurkite atitinkamas
--  lentelės ir susiekite jas One-to-Many ryšiu.

CREATE TABLE Kategorijos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
pavadinimas TEXT(4000)
);

CREATE TABLE Prekes (
id INTEGER PRIMARY KEY AUTOINCREMENT,
pavadinimas TEXT,
aprasymas TEXT,
kategorijos_id INTEGER REFERENCES Kategorijos(id)
);

-- Trečia užduotis
-- Sukurkite duomenų bazę, kurioje saugosite informaciją apie
--  darbuotojus ir jų vadovus. Kiekvienas darbuotojas turi tik
--  vieną vadovą, tačiau kiekvienas vadovas gali turėti daug
--  darbuotojų. Sukurkite atitinkamas lentelės ir susiekite
--  jas One-to-Many ryšiu.

CREATE TABLE Darbuotojas (
id INTEGER PRIMARY KEY AUTOINCREMENT,
vardas VARCHAR(50),
pavarde VARCHAR(50),
el_pastas VARCHAR(100),
telefonas VARCHAR(20)
);

CREATE TABLE Vadovas (
vardas VARCHAR(50),
pavarde VARCHAR(50),
el_pastas VARCHAR(100),
telefonas VARCHAR(20),
fk_vadovas_id INTEGER REFERENCES Vadovas(id)
);

-- Ketvirta užduotis
-- Sukurkite duomenų bazę, kurioje saugosite informaciją apie skelbimus
-- ir jų kategorijas. Kiekvienas skelbimas gali priklausyti daugeliui 
-- kategorijų, ir kiekviena kategorija gali turėti daug skelbimų. 
-- Sukurkite atitinkamas lentelės ir susieti jas Many-to-Many ryšiu.

CREATE TABLE sk_kategorijos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
pavadinimas TEXT(4000)
);

CREATE TABLE skelbimai (
id INTEGER PRIMARY KEY AUTOINCREMENT,
pavadinimas TEXT,
aprasymas TEXT
);

CREATE TABLE skelbimu_kategorijos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fk_skelbimai_id INTEGER REFERENCES skelbimai(id),
fk_sk_kategorijos_id INTEGER REFERENCES sk_kategorijos(id)
);