//Gandirea tabelei
//in momentul in care am creat tabela am gandit-o in felul urmator
//in tabela medicamente, medicamentele pot avea sau nu id, adica sunt 
//destinate unui client sau nu 
//in comenzi sunt medicamente care sunt predestinate sa fie primite clientilor

use Farmacie
go

INSERT INTO Clienti (idClient,Nume, varsta) values
(1,'Balint Leonard',21),
(2,'Anghel Andra', 20),
(3,'Ardelean Andrada',21),
(4,'Baciu Ioana',20);

Select * from Clienti;

INSERT INTO Medicamente (idMedicament, Nume, Cantitate, Pret, idClient) values
(6,'Aspacardin',1,16,3),
(7,'Aspacardin',1,16,1),
(8,'Aspacardin',1,16,2);

Select * from Medicamente;
Select * from Distribuitori;

INSERT INTO Distribuitori (idDistribuitor, Nume) values
(2,'Sandoz');
(1,'Terapia');

Select * from Distribuitori;

INSERT INTO Medicamente_Distribuitori(idDistribuitor, idMedicament) values
(1,6),
(1,7),
(1,8);
(4,9);
(2,4);


Select * from Medicamente;
Select * from Distribuitori;
Select * from Medicamente_Distribuitori;


CREATE PROCEDURE AdaugaSectiune @idManager INT, @Nume VARCHAR(100) 
AS
BEGIN
INSERT INTO Manager(idManager, Nume)
VALUES (@idManager, @Nume);
END
GO

EXEC AdaugaSectiune '1', 'Balint Leonard'
GO

Select * from Manager;

CREATE PROCEDURE AdaugaSectiuneClienti @idClient INT, @Nume VARCHAR(100), @Varsta INT
AS
BEGIN
INSERT INTO Clienti(idClient, Nume, Varsta)
VALUES (@idClient, @Nume, @Varsta);
END
GO

EXEC AdaugaSectiuneClienti '5', 'Bisu Carmen', 30
GO
EXEC AdaugaSectiuneClienti '6', 'Marinel Marin', 19
GO

Select * from Clienti;

CREATE PROCEDURE AdaugaSectiuneAngajati @idAngajati INT, @Nume VARCHAR(100), @idManager INT
AS BEGIN
INSERT INTO Angajati(idAngajati,Nume,idManager)
VALUES (@idAngajati, @Nume, @idManager)
END
GO

EXEC AdaugaSectiuneAngajati '1','Balint Leonard', '1'
GO

EXEC AdaugaSectiuneAngajati '2',' Bisu Carmen', NULL
GO

EXEC AdaugaSectiuneAngajati '3', 'Marinel Marin', NULL
GO

Select * from Angajati;

CREATE PROCEDURE AdaugaSectiuneMagazin @idAngajati INT, @idClient INT
AS 
BEGIN
INSERT INTO Magazin(idAngajati,idClient)
VALUES (@idAngajati, @idClient)
END
GO

Select * from Angajati;
Select * from Clienti;

EXEC AdaugaSectiuneMagazin '1', '1'
GO

Exec AdaugaSectiuneMagazin '2', '5'
Go

Exec AdaugaSectiuneMagazin '3', '6'
Go 

Select * from Magazin;

insert into Comenzi(idComanda, Data_Livrare, numeComenzi, idClient) values
('2','2002-3-10','Pastile durere', '5');
('1','2002-03-14','Pastile raceala','1');

Select * from Clienti;
Select * from Comenzi;

Create procedure AdaugaSectiuneMedicamente @idMedicament int, @Nume varchar(100), @Cantitate int, @Pret int, @idClient int
As 
begin
insert into Medicamente(idMedicament, Nume, Cantitate, Pret, idClient)
values (@idMedicament, @Nume, @Cantitate, @Pret, @idClient)
end
go

select * from Medicamente;

execute AdaugaSectiuneMedicamente '9','Bromhexin Atb', 2, 200, NULL
go

execute AdaugaSectiuneMedicamente '10', 'Amoxicilina Atb', 1, 10, NULL
go

execute AdaugaSectiuneMedicamente '11', 'Paracetamol', 2, 10, NULL
go

select * from Medicamente;

insert into Anti_Biotic(idAnti_Biotic,Nume,Data_Expirare) values
('3','Bromhexin Atb','2002');
('1','Paracetamol','2023'),
('2','Armoxicilina Atb','2023');

Select * from Anti_Biotic;
Select * from Medicamente;

insert into Anti_Biotic_Medicamente(idMedicament,idAnti_Biotic) values
('10','2'),
('9','3'),
('11','1');

select * from Anti_Biotic_Medicamente;

select * from Alergii;
select * from Medicamente;

exec AdaugaSectiuneMedicamente '12', 'Reactin', 2, 20, Null
go
exec AdaugaSectiuneMedicamente '13', 'Claritine', 1, 10, Null
go

insert into Alergii(idAlergii, Nume, Data_Expirare) values
('1', 'Reactin','2002'),
('2', 'Claritine','2009');

select * from Alergii;
select * from Medicamente;
select * from Alergii_Medicamente;

insert into Alergii_Medicamente(idMedicament, idAlergii) values
(12,1),
(13,2);