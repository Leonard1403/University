use Farmacie 


CREATE Or Alter View View1 as
Select * 
FROM Alergii --1pk
GO 

Create Or ALter View View2 as
Select *
From Medicamente --1pk 1fk
GO

Create or Alter View View3 as 
Select * 
From Alergii_Medicamente --2pk

INSERT into TABLES(Name) values
('Alergii'),('Medicamente'),('Alergii_Medicamente')
INSERT INTO Views(Name) values
('View1'),('View2'),('View3')

SELECT * FROM Tables
SELECT * FROM Views

Create or Alter Procedure insertAlergii
As
Declare @n int
Declare @t varchar(30)
Declare @NoOFRows int

Select Top 1 @NoOFRows = NoOFRows From dbo.TestTables
Set @n = 3
While @n<@NoOFRows+3
Begin
Set @t = 'Nume' + CONVERT(Varchar(5), @n)
Insert INTO Alergii (idAlergii,Nume,Data_Expirare) values(@n,@t,'2022-12-12')
Set @n = @n  + 1
End
Go

Create or Alter Procedure insertMedicamente
AS
Declare @n int
Declare @t Varchar(30)
Declare @fk int
Declare @NoOFRows int
Select Top 1 @fk = 1
Set @n = 15
Select Top 1 @NoOFRows = NoOFRows From dbo.TestTables

While @n < @NoOFRows
Begin 
Insert Into Medicamente(idMedicament,Nume,Cantitate,Pret,idClient) Values (@n,'Balbal',1,10,@fk)
Set @n = @n + 1
End
GO

Create or Alter Procedure insertAlergiiMedicamente
As
	Insert Into Alergii_Medicamente
	Select 
	idMedicament = m.idMedicament,
	idAlergii = a.idAlergii
	From Medicamente AS m
	Cross join Alergii As a
Go

Create or Alter Procedure Delete_Table @TableID Int as
	IF(@TableID = 1)
		Begin 
		Delete From Alergii_Medicamente
		Delete From Alergii
		End
	IF(@TableID = 2)
		Begin
		Delete From Alergii_Medicamente
		Delete From Medicamente where idClient = 1
		End
	IF(@TableID = 3)
		Begin
		Delete From Alergii_Medicamente
		End
Go

Create or Alter Procedure Insert_Table @TableID Int as
	IF(@TableID = 1)
		Begin
		Exec insertAlergii
		End
	IF(@TableID = 2)
		Begin
		Exec insertMedicamente
		End
	IF(@TableID = 3)
		Begin
		Exec insertAlergii
		Exec insertMedicamente
		Exec insertAlergiiMedicamente
		End
Go

CREATE Or Alter PROCEDURE Select_View @ViewID INT AS
	IF(@ViewID = 1)
		BEGIN
		SELECT * FROM View1
		END
	IF(@ViewID = 2)
		BEGIN
		SELECT * FROM View2
		END
	IF(@ViewID = 3)
		BEGIN
		SELECT * FROM View3
		END
GO
--////////////////////////////////////////////////////////////

INSERT INTO Tests VALUES ('Delete_Table'), ('Insert_Table'), ('Select_View')
INSERT INTO TestViews VALUES (3,1), (3,2), (3,3)
INSERT INTO TestTables(TestID, TableID, NoOfRows, Position) VALUES 
(2,1,100,1),(2,2,100,2),(2,3,100,3),(1,3,100,4),(1,2,100,5),(1,1,100,6)

--/////////////////////////////////////////////////////////////////
Create or ALTER PROCEDURE TestRunAlergii AS
DECLARE @ds DATETIME
DECLARE @di DATETIME
DECLARE @de DATETIME

SET @ds = GETDATE()
EXEC Delete_Table 1;
EXEC Insert_Table 1;
SET @di = GETDATE()

SELECT * FROM View1
SET @de = GETDATE()
SELECT DATEDIFF(millisecond,@de,@ds) AS	DateDiff

Insert into TestRuns VALUES ('Se sterg elemente din tabela 1 si din celelalte tabele care au elemente din tabela 1, iar apoi se introduc interogari in tabela 1',@ds, @de)
DECLARE @a INT
SELECT @a = TestRunID FROM dbo.TestRuns WHERE StartAt = @ds AND EndAt = @de
Insert into TestRunTables VALUES (@a, 1, @ds, @di)
Insert into TestRunViews VALUES (@a, 1, @di, @de)
GO

--/////////////////////////////////////////////////////////////////
Create or ALTER PROCEDURE TestRunAlergiiMedicamente AS
DECLARE @ds DATETIME
DECLARE @di DATETIME
DECLARE @de DATETIME

SET @ds = GETDATE()
EXEC Delete_Table 3;
EXEC Insert_Table 3;
SET @di = GETDATE()

SELECT * FROM View3
SET @de = GETDATE()
SELECT DATEDIFF(millisecond,@de,@ds) AS	DateDiff

Insert into TestRuns VALUES ('Se sterg elemente din tabela 3 si din celelalte tabele care au elemente din tabela 3, iar apoi se introduc interogari in tabela 3 si in tabele inrudite cu tabela 3',@ds, @de)
DECLARE @a INT
SELECT @a = TestRunID FROM dbo.TestRuns WHERE StartAt = @ds AND EndAt = @de
Insert into TestRunTables VALUES (@a, 3, @ds, @di)
Insert into TestRunViews VALUES (@a, 3, @di, @de)
GO

--////////////////////////////////////////////////////
Create or ALTER PROCEDURE TestRunMedicamente AS
DECLARE @ds DATETIME
DECLARE @di DATETIME
DECLARE @de DATETIME

SET @ds = GETDATE()
EXEC Delete_Table 2;
EXEC Insert_Table 2;
SET @di = GETDATE()

SELECT * FROM View2
SET @de = GETDATE()
SELECT DATEDIFF(millisecond,@de,@ds) AS	DateDiff

Insert into TestRuns VALUES ('Se sterg elemente din tabela 2 si din celelalte tabele care au elemente din tabela 2, iar apoi se introduc interogari in tabela 2 si in tabele inrudite cu tabela 2',@ds, @de)
DECLARE @a INT
SELECT @a = TestRunID FROM dbo.TestRuns WHERE StartAt = @ds AND EndAt = @de
Insert into TestRunTables VALUES (@a, 2, @ds, @di)
Insert into TestRunViews VALUES (@a, 2, @di, @de)
GO
--/////////////////////////////////////////////////
EXEC TestRunAlergii
GO
EXEC TestRunMedicamente
GO
EXEC TestRunAlergiiMedicamente
GO

SELECT * FROM TestRuns
SELECT * FROM TestRunTables
SELECT * FROM TestRunViews