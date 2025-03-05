use Problema1
go

SET TRANSACTION ISOLATION LEVEL READ COMMITTED; --COMMITED
BEGIN TRAN;
SELECT * FROM Briose;
WAITFOR DELAY '00:00:08'
SELECT * FROM Briose;
COMMIT TRAN;

select * from Briose

SELECT CURRENT_TIMESTAMP;
select nume_briosa from Briose order by nume_briosa 
SELECT CURRENT_TIMESTAMP;
create index index1 on Briose(nume_briosa)
drop index Briose.index1
