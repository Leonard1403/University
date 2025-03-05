Use Farmacie
Go

CREATE OR ALTER PROCEDURE Non_Repeatable_Reads_T1 AS
BEGIN
	BEGIN TRAN
	BEGIN TRY
		WAITFOR DELAY '00:00:05'
		UPDATE Clienti SET Nume = 'Miau Miau' WHERE varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Clienti', CURRENT_TIMESTAMP)
		COMMIT TRAN
		SELECT 'Transaction committed' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction rollbacked' AS [Message]
	END CATCH
END

EXECUTE Non_Repeatable_Reads_T1;

Select * from Clienti
Select * from LogTable