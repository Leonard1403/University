USE Farmacie;
GO

CREATE PROCEDURE Non_Repeatable_Reads_T2 AS
BEGIN
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	BEGIN TRAN
	BEGIN TRY
		SELECT * FROM Clienti WHERE varsta = 20
			INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:10'
		SELECT * FROM Clienti WHERE varsta = 20
			INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		COMMIT TRAN
		SELECT 'Transaction committed' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction rollbacked' AS [Message]
	END CATCH
END

EXECUTE Non_Repeatable_Reads_T2;

-- Solution
GO
CREATE PROCEDURE Non_Repeatable_Reads_T2_Solution AS
BEGIN
	SET TRANSACTION ISOLATION LEVEL REPEATABLE READ
	BEGIN TRAN
	BEGIN TRY
		SELECT * FROM Clienti WHERE varsta = 20
			INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:10'
		SELECT * FROM Clienti WHERE varsta = 20
			INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		COMMIT TRAN
		SELECT 'Transaction committed' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction rollbacked' AS [Message]
	END CATCH
END

EXECUTE Non_Repeatable_Reads_T2_Solution;

