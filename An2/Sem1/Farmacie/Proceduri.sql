USE Farmacie
GO

/*Modificare coloana Pret in tip float*/
CREATE OR ALTER PROCEDURE do_proc_1
AS
BEGIN
	Alter table Medicamente 
	Alter Column Pret float
	/*------------------------------------------------------*/
	PRINT 'Done do_proc_1'
	UPDATE Versiune 
	Set versiuneNO = 1
	where versiuneNO = 0
END
GO

/*Adaugare constrangere de pret sa fie cel putin 1*/
CREATE OR ALTER PROCEDURE do_proc_2
AS
BEGIN
	/*
	ALTER TABLE Medicamente 
	ADD DEFAULT 1 FOR Pret;

	ALTER TABLE Medicamente
	ADD CONSTRAINT df_1 DEFAULT 1 FOR Pret
	*/

	ALTER TABLE Medicamente
	Add constraint df_Pret
	Default 1 for Pret;

	/*------------------------------------------------------*/
	PRINT 'Done do_proc_2'
	UPDATE Versiune 
	Set versiuneNO = 2
	where versiuneNO = 1
END
GO

/*Creare tabela seminte*/
CREATE OR ALTER PROCEDURE do_proc_3
AS
BEGIN
	Create Table Seminte(
		idSeminte int Not Null Primary Key,
		Nume varchar(50) Not Null,
	);
	/*------------------------------------------------------*/
	PRINT 'Done do_proc_3'
	UPDATE Versiune 
	Set versiuneNO = 3
	where versiuneNO = 2
END
GO

/*Adaugare coloana de pret in tabela seminte*/
CREATE OR ALTER PROCEDURE do_proc_4
AS
BEGIN
	Alter Table Seminte
	Add Pret int not null
	/*------------------------------------------------------*/
	PRINT 'Done do_proc_4'
	UPDATE Versiune 
	Set versiuneNO = 4
	where versiuneNO = 3
END
GO

/*Creare constrangere dintre idSeminte si idMedicament*/
CREATE OR ALTER PROCEDURE do_proc_5
AS
BEGIN
	Alter table Seminte
	Add constraint fk_Medicamente_Seminte foreign key(idSeminte) References Medicamente(idMedicament)
	/*------------------------------------------------------*/
	PRINT 'Done do_proc_5'
	UPDATE Versiune 
	Set versiuneNO = 5
	where versiuneNO = 4
END
GO

CREATE OR ALTER PROCEDURE undo_proc_1
AS
BEGIN
	Alter table Medicamente 
	Alter Column Pret int
	/*------------------------------------------------------*/
	PRINT 'Done undo_proc_1'
	UPDATE Versiune 
	Set versiuneNO = 0
	where versiuneNO = 1
END
GO

CREATE OR ALTER PROCEDURE undo_proc_2
AS
BEGIN
	ALTER TABLE Medicamente
	Drop constraint df_Pret;
	/*------------------------------------------------------*/
	PRINT 'Done undo_proc_2'
	UPDATE Versiune 
	Set versiuneNO = 1
	where versiuneNO = 2
END
GO


CREATE OR ALTER PROCEDURE undo_proc_3
AS
BEGIN
	Drop Table Seminte
	/*------------------------------------------------------*/
	PRINT 'Done undo_proc_3'
	UPDATE Versiune 
	Set versiuneNO = 2
	where versiuneNO = 3
END
GO

CREATE OR ALTER PROCEDURE undo_proc_4
AS
BEGIN
	Alter table Seminte
	Drop Column Pret
	/*------------------------------------------------------*/
	PRINT 'Done undo_proc_4'
	UPDATE Versiune 
	Set versiuneNO = 3
	where versiuneNO = 4
END
GO

CREATE OR ALTER PROCEDURE undo_proc_5
AS
BEGIN
	Alter Table Seminte
	Drop Constraint fk_Medicamente_Seminte;
	/*------------------------------------------------------*/
	PRINT 'Done undo_proc_5'
	UPDATE Versiune 
	Set versiuneNO = 4
	where versiuneNO = 5
END
GO

CREATE OR ALTER PROCEDURE Main @vers int
AS 
BEGIN
	DECLARE @versiuneNO int
	SET @versiuneNO = (Select * From Versiune)
	Print('Versiunea curenta a tabelei')
	Print(@versiuneNO)
	IF(@versiuneNO = @vers)
		print('Versiunea este aceeasi')
	ELSE IF(@vers > 5 OR @vers < 0)
		print('Versiunea primita nu poate fi efectuata')
	/*Caz 1 - versiunea pe care am primit-o este mai mare decat versiunea tabelei
	  in acest caz trb sa facem update la tabela pana la versiunea ceruta*/
	ELSE IF(@versiuneNO < @vers)
		BEGIN
		Print('Se face Update la tabela')
		if(@versiuneNO = 0 AND @versiuneNO != @vers)
			Begin
			EXEC do_proc_1
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 1 AND @versiuneNO != @vers)
			Begin
			EXEC do_proc_2
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 2 AND @versiuneNO != @vers)
			Begin
			EXEC do_proc_3
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 3 AND @versiuneNO != @vers)
			Begin
			EXEC do_proc_4
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 4 AND @versiuneNO != @vers)
			Begin
			EXEC do_proc_5
			End
		SET @versiuneNO = (Select * From Versiune)

		END
	/*Caz 2 - versiunea pe care am primit-o este mai mica decat versiunea tabelei
	  in acest caz trb sa facem undo la tabela pana la versiunea ceruta*/
	ELSE 
		BEGIN
		Print('Se face Undo la tabela')
		if(@versiuneNO = 5 AND @versiuneNO != @vers)
			Begin
			EXEC undo_proc_5
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 4 AND @versiuneNO != @vers)
			Begin
			EXEC undo_proc_4
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 3 AND @versiuneNO != @vers)
			Begin
			EXEC undo_proc_3
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 2 AND @versiuneNO != @vers)
			Begin
			EXEC undo_proc_2
			End
		SET @versiuneNO = (Select * From Versiune)

		if(@versiuneNO = 1 AND @versiuneNO != @vers)
			Begin
			EXEC undo_proc_1
			End
		SET @versiuneNO = (Select * From Versiune)
		END

	Print('Versiunea dupa modificare a tabelei')
	Print(@versiuneNO)
END
GO


/*
EXEC do_proc_1
EXEC do_proc_2
EXEC do_proc_3
EXEC do_proc_4
EXEC do_proc_5

EXEC undo_proc_1
EXEC undo_proc_2
EXEC undo_proc_3
EXEC undo_proc_4
EXEC undo_proc_5
*/

EXEC Main -1


Create table Versiune
(
versiuneNO int
)


Select * 
From Versiune

/*
EXECUTE [dbo].[sp_help] 'Medicamente'
GO

EXECUTE [dbo].[sp_help] 'Seminte'
GO

EXECUTE [dbo].[sp_helpconstraint] 'Medicamente'
GO

ALTER TABLE [dbo].[Medicamente]
DROP CONSTRAINT DF__Medicament__Pret__151B244E
GO
*/
