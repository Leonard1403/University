use S1
go

--dirty reads
BEGIN TRAN
UPDATE Profesori SET Nume='dirty reads'
WAITFOR DELAY '00:00:05'
ROLLBACK TRAN

select * from Profesori