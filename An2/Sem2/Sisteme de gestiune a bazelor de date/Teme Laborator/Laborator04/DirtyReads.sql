use Farmacie
go

CREATE OR ALTER PROCEDURE DirtyReads_T1 AS
BEGIN
	SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
	BEGIN TRAN
	BEGIN TRY
		SELECT * FROM Clienti WHERE varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:10'
		SELECT * FROM Clienti where varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		COMMIT TRAN
		SELECT 'Transaction committed' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction rollbacked' AS [Message]
	END CATCH
END;

Execute DirtyReads_T1;

CREATE OR ALTER PROCEDURE DirtyReads_T1_Solution AS
BEGIN
	SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	BEGIN TRAN
	BEGIN TRY
		SELECT * FROM Clienti where varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		WAITFOR DELAY '00:00:10'
		SELECT * FROM Clienti where varsta = 20
		INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('SELECT', 'Clienti', CURRENT_TIMESTAMP)
		COMMIT TRAN
		SELECT 'Transaction committed' AS [Message]
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		SELECT 'Transaction rollbacked' AS [Message]
	END CATCH
END;

Execute DirtyReads_T1_Solution;

Select * from Clienti
Select * from LogTable