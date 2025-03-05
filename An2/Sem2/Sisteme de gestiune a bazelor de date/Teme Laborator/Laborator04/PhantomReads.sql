Use Farmacie
go

CREATE OR ALTER PROCEDURE Phantom_Reads_T1 AS
BEGIN
BEGIN TRAN
BEGIN TRY
WAITFOR DELAY '00:00:05'
INSERT INTO Clienti (idClient, Nume, varsta) VALUES (100, 'John Cena', 96);
INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('INSERT', 'Clienti', CURRENT_TIMESTAMP)
COMMIT TRAN
SELECT 'Transaction committed' AS [Message]
END TRY
BEGIN CATCH
ROLLBACK TRAN
SELECT 'Transaction rollbacked' AS [Message]
END CATCH
END

EXECUTE Phantom_Reads_T1;

CREATE PROCEDURE DeleteClient
@idClient INT
AS
BEGIN
BEGIN TRY
DELETE FROM Clienti WHERE idClient = @idClient;
INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('DELETE', 'Clienti', CURRENT_TIMESTAMP);
SELECT 'Row deleted successfully!' AS [Message];
END TRY
BEGIN CATCH
SELECT 'Error occurred. Transaction rollbacked.' AS [Message];
ROLLBACK;
END CATCH;
END;

EXECUTE DeleteClient @idClient = 100;

Select * from Clienti
