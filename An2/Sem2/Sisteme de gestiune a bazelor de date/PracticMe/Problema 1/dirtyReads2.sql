use Problema1
go

--dirty reads
BEGIN TRAN
UPDATE Briose SET nume_briosa='dirty reads'
WAITFOR DELAY '00:00:05'
ROLLBACK TRAN

select * from Briose