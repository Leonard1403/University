use Problema3
go

BEGIN TRAN
WAITFOR DELAY '00:00:05'
INSERT INTO Biscuiti(nume_b,nr_calorii,pret,cod_p) VALUES 
('Phantom Reads',50,5,3)
Commit Tran

select * from Biscuiti
Delete from Biscuiti where nume_b = 'Phantom Reads'

select nume_b from Biscuiti order by nume_b
create index index1 on Biscuiti(nume_b)
drop index Biscuiti.index1