use Farmacie
go

CREATE TABLE LogTable (
  operatia VARCHAR(20),
  tabel VARCHAR(20),
  timpul TIMESTAMP
);

ALTER TABLE LogTable
ALTER COLUMN timpul DATETIME;

Select * from LogTable

Create table Clienti
(idClient INT PRIMARY KEY,
Nume varchar(60),
varsta int)

Create table Comenzi
(idComanda INT PRIMARY KEY,
Data_Livrare date,
numeComenzi varchar(60),
idClient INT FOREIGN KEY REFERENCES Clienti(idClient))

--DeadLock

Select * from Clienti
Select * from Comenzi

UPDATE Comenzi 
        SET Data_Livrare = DATEADD(DAY, -10, GETDATE()) -- Modificarea datelor comenzilor pentru a crea un deadlock
        WHERE Data_Livrare < GETDATE();

UPDATE Clienti 
        SET Nume = 'Mioara Alin' -- Modificarea datelor clientilor pentru a crea un deadlock
        WHERE idClient IN (
            SELECT idClient 
            FROM Comenzi 
            WHERE Data_Livrare < GETDATE()
        );

-- Dirty reads:
SELECT * FROM Clienti