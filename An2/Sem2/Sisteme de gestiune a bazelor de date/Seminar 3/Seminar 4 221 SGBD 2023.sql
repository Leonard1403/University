USE Seminar2SGBD2212023;
SELECT * FROM sys.dm_tran_locks;
SELECT DB_NAME(207);
BEGIN TRAN;
SELECT * FROM Jocuri;
SELECT * FROM sys.dm_tran_locks;
SELECT * FROM Jocuri;
UPDATE Jocuri SET pret=0 WHERE nume='StarCraft 2';
SELECT * FROM sys.dm_tran_locks;
SELECT * FROM Jocuri;
SELECT * FROM sys.dm_tran_locks;
ROLLBACK TRAN;
SELECT * FROM sys.dm_tran_locks;
SELECT * FROM Jocuri;
SELECT * FROM sys.dm_tran_active_transactions
BEGIN TRAN;
SELECT * FROM Jocuri;
SELECT * FROM sys.dm_tran_active_transactions
COMMIT TRAN;
SELECT * FROM sys.dm_tran_active_transactions;