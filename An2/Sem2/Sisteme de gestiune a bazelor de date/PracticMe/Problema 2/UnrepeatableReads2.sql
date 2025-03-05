use Problema2
go

--Non-repeatable reads
INSERT INTO Melodii(titlu,an_lansare,durata,cod_artist) VALUES 
('Alejandro',2009,'00:03:45.0000000',1)
BEGIN TRAN
WAITFOR DELAY '00:00:05'
UPDATE Melodii SET an_lansare=2008 WHERE titlu='Alejandro'
COMMIT TRAN

Delete From Melodii where titlu = 'Alejandro'

select titlu from Melodii order by titlu
create index index1 on Melodii(titlu)
drop index Melodii.index1

select * from Melodii