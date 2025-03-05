Use Farmacie
go

/*
Create table Medicamente
(idMedicament INT PRIMARY KEY,
Nume varchar(60),
Cantitate int Check (Cantitate=1 Or Cantitate=2),
Pret int,
idClient int FOREIGN KEY REFERENCES Clienti(idClient))

Create table Anti_Biotic
(idAnti_Biotic INT PRIMARY KEY,
Nume varchar(60),
Data_Expirare date)

Create table Anti_Biotic_Medicamente
(idMedicament INT FOREIGN KEY REFERENCES Medicamente(idMedicament),
idAnti_Biotic INT FOREIGN KEY REFERENCES Anti_Biotic(idAnti_Biotic),
CONSTRAINT pk_Anti_Biotic_Medicamente PRIMARY KEY(idMedicament, idAnti_Biotic))
*/

Select * From Medicamente
Select * From Anti_Biotic
Select * From Anti_Biotic_Medicamente

GO
CREATE FUNCTION dbo.CheckMedicamentData (@nume varchar(60), @cantitate int, @pret int, @idClient int)
RETURNS bit
AS
	BEGIN
		DECLARE @result bit
		IF (@nume IS NOT NULL AND @cantitate IN (1,2) AND @pret >= 0 AND @pret <= 1000)
		SET @result = 1
		ELSE
		SET @result = 0
	RETURN @result
END
GO

SELECT dbo.CheckMedicamentData('Nurofen', 1, 10, 123) AS 'Test 1 (expected result 1)'
SELECT dbo.CheckMedicamentData(NULL, 2, 20, 456) AS 'Test 2 (expected result 0)'
SELECT dbo.CheckMedicamentData('Paracetamol', 2, 30, NULL) AS 'Test 3 (expected result 1)'
SELECT dbo.CheckMedicamentData('Aspirin', 4, -40, 789) AS 'Test 4 (expected result 0)'
SELECT dbo.CheckMedicamentData('Ibuprofen', 2, 50, 234) AS 'Test 5 (expected result 1)'

CREATE OR ALTER FUNCTION dbo.CheckAntiBioticData (@nume varchar(60), @data_expirare date)
RETURNS bit
AS
	BEGIN
		DECLARE @result bit
		IF (@nume IS NOT NULL AND @data_expirare >= GETDATE())
			SET @result = 1
		ELSE
			SET @result = 0
RETURN @result
END
GO

SELECT dbo.CheckAntiBioticData('Paracetamol', '2024-01-01') as Result1 -- rezultat: 1
SELECT dbo.CheckAntiBioticData('Ibuprofen', '2023-06-01') as Result2 -- rezultat: 1
SELECT dbo.CheckAntiBioticData(NULL, '2022-01-01') as Result3 -- rezultat: 0
SELECT dbo.CheckAntiBioticData('Amoxicilina', NULL) as Result4 -- rezultat: 0

CREATE TABLE LogTable
(
	idLog INT IDENTITY PRIMARY KEY,
	operatia VARCHAR(50),
	tabel VARCHAR(50),
	timpul DATE
)

CREATE OR ALTER PROCEDURE AddMedicamentAntiBiotic 
@nume_medicament varchar(60),
@cantitate int,
@pret int,
@idClient int,
@nume_antibiotic varchar(60),
@data_expirare date
AS
BEGIN
	BEGIN TRAN
	BEGIN TRY
		IF (dbo.CheckMedicamentData(@nume_medicament, @cantitate, @pret, @idClient) = 0)
		BEGIN
			Select 'Invalid data for Medicament'
			RAISERROR('Invalid data for Medicament', 14, 1)
		END
		IF (dbo.CheckAntiBioticData(@nume_antibiotic, @data_expirare) = 0)
		BEGIN
			Select 'Invalid data for Anti-Biotic'
			RAISERROR('Invalid data for Anti-Biotic', 14, 1)
		END

		DECLARE @id_medicament INT
		DECLARE @id_antibiotic INT
		
		SELECT @id_medicament = MAX(idMedicament) from Medicamente
		SET @id_medicament = @id_medicament + 1

		SELECT @id_antibiotic = MAX(idAnti_Biotic) from Anti_Biotic
		SET @id_antibiotic = @id_antibiotic + 1

		INSERT INTO Medicamente (idMedicament, Nume, Cantitate, Pret, idClient) VALUES (@id_medicament, @nume_medicament, @cantitate, @pret, @idClient)
		INSERT INTO Anti_Biotic (idAnti_Biotic, Nume, Data_Expirare) VALUES (@id_antibiotic, @nume_antibiotic, @data_expirare)
		INSERT INTO Anti_Biotic_Medicamente (idMedicament, idAnti_Biotic) VALUES (@id_medicament, @id_antibiotic)
		INSERT INTO LogTable (operatia, tabel, timpul) VALUES ('Adaugare', 'Anti_Biotic_Medicamente', GETDATE())

		COMMIT TRAN
		SELECT 'Transaction committed'
	END TRY
	BEGIN CATCH

		ROLLBACK TRAN
		SELECT 'Transaction rollbacked'
	END CATCH
END
GO

Select * from LogTable

Select * From Medicamente
Select * From Anti_Biotic
Select * From Anti_Biotic_Medicamente

-- Test the procedure

EXEC AddMedicamentAntiBiotic 'Nurofen', 1, 15, null, 'Amoxicilina', '2025-05-02'
EXEC AddMedicamentAntiBiotic 'Panadol', 2, 20, 2, 'Clarithromycin', '2024-08-01'
EXEC AddMedicamentAntiBiotic 'Ibuprofen', 1, 25, 3, 'Azithromycin', '2023-12-31'
EXEC AddMedicamentAntiBiotic 'Aspirina', 2, 30, 4, 'Penicillin', '2024-06-15'

-- Test with invalid data for Medicament
EXEC AddMedicamentAntiBiotic '', 3, 25, 3, 'Azithromycin', '2023-12-31'
EXEC AddMedicamentAntiBiotic 'Ibuprofen', 4, 3000, 4, 'Penicillin', '2022-06-15'

-- Test with invalid data for Anti-Biotic
EXEC AddMedicamentAntiBiotic 'Aspirina', 1, 30, 4, '', '2022-06-15'
EXEC AddMedicamentAntiBiotic 'Nurofen', 1, 15, 1, 'Amoxicilina', '2021-05-02'


CREATE OR ALTER PROCEDURE AddMedicamentAntiBiotic2
@nume_medicament varchar(60),
@cantitate int,
@pret int,
@idClient int,
@nume_antibiotic varchar(60),
@data_expirare date
AS 
BEGIN
	DECLARE @inserareOkMedicament INT
	SET @inserareOkMedicament = 0

	DECLARE @maxMedicament INT
	DECLARE @maxAnti_Biotic INT

	BEGIN TRAN
	BEGIN TRY
		IF(dbo.CheckMedicamentData(@nume_medicament, @cantitate, @pret, @idClient) = 0)
		BEGIN
			RAISERROR('Invalid data for Medicament',14,1)
		END

		SELECT @maxMedicament = MAX(idMedicament) FROM Medicamente
		SET @maxMedicament = @maxMedicament + 1

		INSERT INTO Medicamente(idMedicament,Nume,Cantitate,Pret,idClient) VALUES (@maxMedicament, @nume_medicament, @cantitate, @pret, @idClient)

		COMMIT TRAN
		Select 'Transaction Medicamente Commited'
		SET @inserareOkMedicament = 1
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		Select 'Transaction Medicamente Rollbacked'
	END CATCH

	--IF(@inserareOkMedicament <> 0)
	--BEGIN
		DECLARE @inserareOkAnti_Biotic INT
		SET @inserareOkAnti_Biotic = 0

		BEGIN TRAN
		BEGIN TRY
			IF(dbo.CheckAntiBioticData(@nume_antibiotic,@data_expirare) = 0)
			BEGIN
				RAISERROR('Invalid data for Anti_Biotic',14,1)
			END

			SELECT @maxAnti_Biotic = MAX(idAnti_Biotic) From Anti_Biotic
			SET @maxAnti_Biotic = @maxAnti_Biotic + 1

			INSERT INTO Anti_Biotic(idAnti_Biotic,Nume,Data_Expirare) VALUES (@maxAnti_Biotic, @nume_antibiotic, @data_expirare)

			COMMIT TRAN
			Select 'Transaction Anti_Biotic commited'
			SET @inserareOkAnti_Biotic = 1
		END TRY
		BEGIN CATCH
			ROLLBACK TRAN
			SELECT 'Transaction Anti_Biotic Rollbacked'
		END CATCH
	--END

	IF(@inserareOkMedicament <> 0 AND @inserareOkAnti_Biotic <> 0)
	BEGIN
		BEGIN TRAN
		BEGIN TRY
			INSERT INTO Anti_Biotic_Medicamente(idMedicament, idAnti_Biotic) VALUES (@maxMedicament, @maxAnti_Biotic)
			COMMIT TRAN
			SELECT 'Transaction Anti_Biotic_Medicamente commited'
		END TRY
		BEGIN CATCH
			ROLLBACK TRAN
			SELECT 'Transaction Anti_Bitoic_Medicamente rollbacked'
		END CATCH
	END 
	INSERT INTO LogTable (operatia, tabel, timpul) VALUES ('Adaugare', 'Anti_Biotic_Medicamente', GETDATE())
END
GO
-- Test the procedure

EXEC AddMedicamentAntiBiotic2 'Nurofen', 1, 15, null, 'Amoxicilina', '2025-05-02'
EXEC AddMedicamentAntiBiotic2 'Panadol', 2, 20, 2, 'Clarithromycin', '2024-08-01'
EXEC AddMedicamentAntiBiotic2 'Ibuprofen', 1, 25, 3, 'Azithromycin', '2023-12-31'
EXEC AddMedicamentAntiBiotic2 'Aspirina', 2, 30, 4, 'Penicillin', '2024-06-15'

-- Test with invalid data for Medicament
EXEC AddMedicamentAntiBiotic2 '', 3, 25, 3, 'Azithromycin', '2023-12-31'
EXEC AddMedicamentAntiBiotic2 'Ibuprofen', 4, 3000, 4, 'Penicillin', '2022-06-15'

-- Test with invalid data for Anti-Biotic
EXEC AddMedicamentAntiBiotic2 'Aspirina', 4, 30, 4, '', '2022-06-15'
EXEC AddMedicamentAntiBiotic2 'Nurofen', 1, 15, 1, 'Amoxicilina', '2021-05-02'

