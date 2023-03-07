Create database Farmacie
go 
use Farmacie
go

Create table Clienti
(idClient INT PRIMARY KEY,
Nume varchar(60),
varsta int)

Create table Medicamente
(idMedicament INT PRIMARY KEY,
Nume varchar(60),
Cantitate int Check (Cantitate=1 Or Cantitate=2),
Pret int,
idClient int FOREIGN KEY REFERENCES Clienti(idClient))

Create table Distribuitori
(idDistribuitor INT PRIMARY KEY,
Nume varchar(50))

Create table Medicamente_Distribuitori
(idDistribuitor INT FOREIGN KEY REFERENCES Distribuitori(idDistribuitor),
idMedicament INT FOREIGN KEY REFERENCES Medicamente(idMedicament),
CONSTRAINT pk_Medicamente_Distribuitori PRIMARY KEY(idDistribuitor, idMedicament))

Create table Comenzi
(idComanda INT PRIMARY KEY,
Data_Livrare date,
numeComenzi varchar(60),
idClient INT FOREIGN KEY REFERENCES Clienti(idClient))

Create table Manager
(idManager INT PRIMARY KEY, 
Nume varchar(50))

Create table Angajati
(idAngajati INT PRIMARY KEY,
Nume varchar(50),
idManager INT FOREIGN KEY REFERENCES Manager(idManager))

Create table Magazin
(idAngajati INT FOREIGN KEY REFERENCES Angajati(idAngajati),
idClient INT FOREIGN KEY REFERENCES Clienti(idClient),
CONSTRAINT pk_Magazin PRIMARY KEY(idAngajati, idClient))

Create table Anti_Biotic
(idAnti_Biotic INT PRIMARY KEY,
Nume varchar(60),
Data_Expirare date)

Create table Alergii
(idAlergii INT PRIMARY KEY,
Nume varchar(60),
Data_Expirare date)

Create table Anti_Biotic_Medicamente
(idMedicament INT FOREIGN KEY REFERENCES Medicamente(idMedicament),
idAnti_Biotic INT FOREIGN KEY REFERENCES Anti_Biotic(idAnti_Biotic),
CONSTRAINT pk_Anti_Biotic_Medicamente PRIMARY KEY(idMedicament, idAnti_Biotic))

Create table Alergii_Medicamente
(idMedicament INT FOREIGN KEY REFERENCES Medicamente(idMedicament),
idAlergii INT FOREIGN KEY REFERENCES Alergii(idAlergii),
CONSTRAINT pk_Alergii_Medicamente PRIMARY KEY(idMedicament, idAlergii))