--Problema1
--dirty reads
--BEGIN TRAN
--UPDATE Briose SET nume_briosa='dirty reads' WHERE nume_briosa='briosa1 Carpati'
--WAITFOR DELAY '00:00:05'
--ROLLBACK TRAN

--select nume_briosa from Briose order by nume_briosa 
--create index index1 on Briose(nume_briosa)
--drop index Briose.index1






--Problema2
--Non-repeatable reads
--INSERT INTO Melodii(titlu,an_lansare,durata,cod_artist) VALUES 
--('Alejandro',2009,'00:03:45.0000000',1)
--BEGIN TRAN
--WAITFOR DELAY '00:00:05'
--UPDATE Melodii SET an_lansare=2008 WHERE titlu='Alejandro'
--COMMIT TRAN

--select titlu from Melodii order by titlu
--create index index1 on Melodii(titlu)
--drop index Melodii.index1



--Problema3
--Phantom Reads
BEGIN TRAN
WAITFOR DELAY '00:00:05'
INSERT INTO Biscuiti(nume_b,nr_calorii,pret,cod_p) VALUES 
('Phantom Reads',50,5,3)
COMMIT TRAN


select nume_b from Biscuiti order by nume_b
create index index1 on Biscuiti(nume_b)
drop index Biscuiti.index1