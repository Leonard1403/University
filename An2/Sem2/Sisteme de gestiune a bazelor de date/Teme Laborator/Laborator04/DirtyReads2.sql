use Farmacie
go

CREATE OR ALTER PROCEDURE ModifyClients AS
BEGIN
	BEGIN TRY
		BEGIN TRANSACTION
		UPDATE Clienti SET Nume = 'Jhon Cena' WHERE varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:05'
		ROLLBACK TRANSACTION
		SELECT 'Transaction successful!' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRANSACTION
		SELECT 'Transaction failed!' AS [Message]
	END CATCH
END;

GO
CREATE OR ALTER PROCEDURE ModifyClients AS
BEGIN
	BEGIN TRY
		BEGIN TRAN
		UPDATE Clienti SET Nume = 'Dhon Bena' WHERE varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:05'
		ROLLBACK TRAN
		SELECT 'Transaction successful!' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction failed!' AS [Message]
	END CATCH
END;


Execute ModifyClients;

UPDATE Clienti SET Nume = 'Maria Shoun' WHERE varsta = 20

Select * from Clienti Where varsta = 20

Select * from LogTable
