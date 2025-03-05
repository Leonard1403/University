use S1
go

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; --COMMITED
BEGIN TRAN;
SELECT * FROM Profesori;
WAITFOR DELAY '00:00:08'
SELECT * FROM Profesori;
COMMIT TRAN;

Select * from Profesori

SELECT CURRENT_TIMESTAMP;
select * from Profesori order by Nume
SELECT CURRENT_TIMESTAMP;
create index index1 on Profesori(Nume)
drop index Profesori.index1