use Farmacie
go

select * from Medicamente
select * from Anti_Biotic
select * from Anti_Biotic_Medicamente

--Furnizori
--functie de VALIDARE
CREATE or alter FUNCTION TestMedicamente(@nume varchar(50), @cantitate int)
RETURNS INT
AS
	BEGIN
	DECLARE @valid INT
	SET @valid=0
	IF(LEN(@nume)=0 OR len(@cantitate)=0)
		BEGIN
			SET @valid=0
		END
	--if exists(select * from Medicamente where Nume = @nume and Cantitate = @cantitate)
	--	BEGIN
	--		SET @valid=1
	--	END
	--RETURN @valid
	select @valid = 
		   count(*) 
		   from Medicamente 
		   where Nume = @nume and Cantitate = @cantitate
	return @valid
	END
go

select * from Medicamente
select dbo.TestMedicamente('Aspacardin', 1) AS result

--select count(*) from Medicamente where Nume = 'Nurofen Raceala si Gripa' and Cantitate = 2

------------------------------------------------------------------------------------------------

--CREATE
CREATE PROCEDURE insert_Medicamente @Nume VARCHAR(50), @Cantitate int, @Pret float, @idClient INT, @nrOfRows INT
AS
BEGIN
	DECLARE @n int
	DECLARE @idMax int
	DECLARE @id int
	DECLARE @t VARCHAR(30)
	SET @n=1 
	if exists(select * from Medicamente)
		begin
			Select @idMax = max(idMedicament) From Medicamente
		end
	else
		begin
			set @idMax = 0
		end

	WHILE @n<=@nrOfRows
	BEGIN
		SET @id = @idMax + @n
		INSERT INTO Medicamente VALUES (@id, @Nume, @Cantitate, @Pret, @idClient)
		SET @n=@n+1
	end
END

Select * from Medicamente
EXEC insert_Medicamente @Nume ='Nurofen', @Cantitate=1, @Pret=20, @idClient = 1, @nrOfRows = 1
Select * from Medicamente

--READ
SELECT * FROM Medicamente

--UPDATE 
CREATE or Alter PROCEDURE update_Medicamente @Nume VARCHAR(50), @Cantitate int, @Pret float, @idClient INT, 
@NumeNou VARCHAR(50), @CantitateNou int, @PretNou float, @idClientNou INT
AS
BEGIN
	--print(@Nume+' '+@Cantitate+' '+@Pret)
	select * from Medicamente where Nume = @Nume and Cantitate = @Cantitate and Pret = @Pret and idClient = @idClient
	UPDATE Medicamente 
	set Nume=@NumeNou, Cantitate=@CantitateNou, Pret = @PretNou, idClient=@idClientNou
	WHERE Nume = @Nume and Cantitate = @Cantitate and Pret = @Pret and idClient = @idClient
END

--DROP PROCEDURE update_Furnizor

select * from Medicamente
EXEC update_Medicamente 'Nurofen', 1, 20, 1, 'Nurofen', 2, 50, 2
SELECT * FROM Medicamente


--DELETE
CREATE or alter PROCEDURE delete_Medicamente @nume VARCHAR(50)
AS
BEGIN
	declare @id int
	select @id=idMedicament from Medicamente where Nume=@nume

	--Delete From Anti_Biotic_Medicamente from Medicamente M 
	DELETE FROM Anti_Biotic where Nume = @nume
	DELETE FROM Medicamente where Nume=@nume
	Delete from Anti_Biotic_Medicamente where idMedicament = @id
END

Select * from Medicamente
EXEC delete_Medicamente @nume='Nurofen'
Select * from Medicamente

--CRUD MEDICAMENT-------------------------------------------------------------
CREATE or alter PROCEDURE CRUD_Medicamente @Nume VARCHAR(50), @Cantitate int, @Pret float, @idClient INT, @nrOfRows INT AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @nume2 VARCHAR(50)
	DECLARE @cantitate2 int
	DECLARE @pret2 float
	Declare @idClient2 int

	SET @nume2=@Nume+'1'
	SET @cantitate2 = @Cantitate + 1
	SET @pret2 = @Pret + 1
	Set @idClient2 = @idClient + 1

	--test nume medicament
	IF(dbo.TestMedicamente(@Nume,@Cantitate) = 1)
		BEGIN
			--CREATE= INSERT
			EXEC insert_Medicamente @Nume, @Cantitate, @Pret, @idClient, @nrOfRows
			--READ= SELECT
			SELECT * FROM Medicamente
			--UPDATE= UPDATE
			EXEC update_Medicamente @Nume, @Cantitate, @Pret, @idClient, @nume2, @cantitate2, @pret2, @idClient2
			SELECT * FROM Medicamente
			--DELETE= DELETE
			EXEC delete_Medicamente @nume2
			SELECT * FROM Medicamente
			PRINT 'CRUD Operations on table Medicamente'
		END
		ELSE
		BEGIN
			PRINT 'Eroare de validare!'
			RETURN; 
		END
END

select * from Medicamente
insert into Medicamente values(17,'Nurofen',1,20,1)
EXEC CRUD_Medicamente @Nume ='Nurofen', @Cantitate= 1, @Pret =20, @idClient=1, @nrOfRows=3

--------------------------------------------------------------------------------------------------------------

--Anti_Biotic_Medicamente

--functie de VALIDARE
SELECT * FROM Anti_Biotic_Medicamente

CREATE FUNCTION TestAnti_Biotic_Medicamente(@idMedicament Int , @idAnti_Biotic int) 
RETURNS INT
AS
BEGIN
	DECLARE @valid INT
	SET @valid=0--presupunem ca data este corecta
	Select @valid = count(*) from Anti_Biotic_Medicamente where idMedicament = @idMedicament and idAnti_Biotic = @idAnti_Biotic
	RETURN @valid;
END

select * from Anti_Biotic_Medicamente
SELECT dbo.TestAnti_Biotic_Medicamente(9,3) as Result
select count(*) from Anti_Biotic_Medicamente

--CREATE
CREATE or alter PROCEDURE insert_Anti_Biotic_Medicamente @idMedicament Int , @idAnti_Biotic int, @nrOfRows INT
AS
BEGIN
	DECLARE @n int
	DECLARE @idMax int
	DECLARE @id int
	DECLARE @t VARCHAR(30)
	SET @n=1
	if exists(select * from Anti_Biotic_Medicamente)
	begin
		Select @idMax = count(*)+1 From Anti_Biotic_Medicamente
	end
	else
	begin
		set @idMax = 0
	end

	WHILE @n<=@nrOfRows 
	BEGIN
		SET @id = @idMax + @n
		
		INSERT INTO Anti_Biotic_Medicamente VALUES (@idMedicament+@n, @idAnti_Biotic+@n)
		SET @n=@n+1
	end
END

select * from Anti_Biotic_Medicamente
exec insert_Anti_Biotic_Medicamente 1, 1, 1
select * from Anti_Biotic_Medicamente

select * from Medicamente
select * from Anti_Biotic
select * from Anti_Biotic_Medicamente

--insert into Anti_Biotic_Medicamente values(
--insert into Anti_Biotic values(4,'Nurofen','2001-02-02')

EXEC insert_Anti_Biotic_Medicamente @idMedicament = 15, @idAnti_Biotic = 4, @nrOfRows=1

--READ
SELECT * FROM Anti_Biotic_Medicamente


--UPDATE 
CREATE or alter PROCEDURE update_Anti_Biotic_Medicamente @idMedicament Int , @idAnti_Biotic int, 
@idMedicamentNou Int , @idAnti_BioticNou int
AS
BEGIN
	UPDATE Anti_Biotic_Medicamente set idMedicament=@idMedicamentNou, idAnti_Biotic=@idAnti_BioticNou
	WHERE idMedicament=@idMedicament and idAnti_Biotic = @idAnti_Biotic
END

Select * from Anti_Biotic_Medicamente
Exec update_Anti_Biotic_Medicamente 2, 2, 15, 4
Select * from Anti_Biotic_Medicamente


--DELETE
CREATE or alter PROCEDURE delete_Anti_Biotic_Medicamente @idMedicament Int , @idAnti_Biotic int
AS
BEGIN
	delete from Anti_Biotic_Medicamente where idMedicament = @idMedicament and idAnti_Biotic = @idAnti_Biotic
END

Select * from Anti_Biotic_Medicamente
EXEC delete_Anti_Biotic_Medicamente 15,4
Select * from Anti_Biotic_Medicamente


--Crud Anti Biotic Medicamente
CREATE or alter PROCEDURE CRUD_Anti_Biotic_Medicamente @idMedicament Int , @idAnti_Biotic int, @nrOfRows INT AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @idMedicament2 int
	DECLARE @idAnti_Biotic2 int

	SET @idMedicament2= @idMedicament + 1
	SET @idAnti_Biotic2= @idAnti_Biotic + 1
	--test nume pasager
	IF(dbo.TestAnti_Biotic_Medicamente(@idMedicament, @idAnti_Biotic) = 1)
		BEGIN
			--CREATE= INSERT
			EXEC insert_Anti_Biotic_Medicamente @idMedicament, @idAnti_Biotic, @nrOfRows
			select * from Anti_Biotic_Medicamente
			--READ= SELECT
			SELECT * FROM Anti_Biotic_Medicamente
			--UPDATE= UPDATE
			EXEC update_Anti_Biotic_Medicamente @idMedicament, @idAnti_Biotic, 4, 4
			SELECT * FROM Anti_Biotic_Medicamente
			--DELETE= DELETE
			EXEC delete_Anti_Biotic_Medicamente @idMedicament2, @idAnti_Biotic2
			SELECT * FROM Anti_Biotic_Medicamente
			PRINT 'CRUD Operations on table Furnizori'
		END
		ELSE
		BEGIN
			PRINT 'Eroare de validare!'
			RETURN; 
		END
END

select * from Anti_Biotic_Medicamente

insert into Anti_Biotic_Medicamente values(1,1)

exec delete_Anti_Biotic_Medicamente 4, 4
Select * from Anti_Biotic_Medicamente
Exec CRUD_Anti_Biotic_Medicamente 1, 1, 1
Select * from Anti_Biotic_Medicamente

--------------------------------------------------------------------------------------------------------------

select * from Anti_Biotic

--Anti_Biotic
CREATE or alter FUNCTION TestAnti_Biotic(@idAnti_Biotic int, @Nume VARCHAR(50))
RETURNS INT
AS
	BEGIN
	DECLARE @valid INT
	SET @valid=0
	select @valid = count(*) from Anti_Biotic where idAnti_Biotic = @idAnti_Biotic and Nume = @Nume
	--if exists(select * from Furnizori where IDfurnizor=@id)
		--BEGIN
			--SET @valid=0
		--END
	RETURN @valid
	END
go

select * from Anti_Biotic

select dbo.TestAnti_Biotic(4,'Nurofen') as Result

--CREATE
CREATE PROCEDURE insert_Anti_Biotic @idAnti_Biotic int, @Nume VARCHAR(50), @Data_Expirare date, @nrOfRows INT
AS
BEGIN
	DECLARE @n int
	DECLARE @idMax int
	DECLARE @id int
	DECLARE @t VARCHAR(30)
	SET @n=1 
	if exists(select * from Anti_Biotic)
	begin
		Select @idMax = max(idAnti_Biotic) From Anti_Biotic
	end
	else
	begin
		set @idMax = 0
	end

	WHILE @n<=@nrOfRows 
	BEGIN
		SET @id = @idMax + @n
		
		INSERT INTO Anti_Biotic VALUES (@idAnti_Biotic+@n-1, @Nume+'1', @Data_Expirare)
		SET @n=@n+1
	end
END

select * From Anti_Biotic
EXEC insert_Anti_Biotic 30,'Nurofen','2020-03-14',2
select * from Anti_Biotic


--READ
SELECT * FROM Anti_Biotic


--UPDATE 
CREATE PROCEDURE update_Anti_Biotic @idAnti_Biotic int, @Nume VARCHAR(50), @Data_Expirare date, 
@idAnti_BioticNou int, @NumeNou VARCHAR(50), @Data_ExpirareNou date
AS
BEGIN
	UPDATE Anti_Biotic set idAnti_Biotic = @idAnti_BioticNou, Nume = @NumeNou, Data_Expirare = @Data_ExpirareNou
	WHERE idAnti_Biotic = @idAnti_Biotic and Nume = @Nume and Data_Expirare = @Data_Expirare
END

--DROP PROCEDURE update_Furnizor

select * from Anti_Biotic
EXEC update_Anti_Biotic 10, 'Nurofen', '2020-03-14', 100, 'Nurofen 20', '2020-03-14'
select * from Anti_Biotic

--DELETE
CREATE or alter PROCEDURE delete_Anti_Biotic @idAnti_Biotic int
AS
BEGIN
	delete from Anti_Biotic where idAnti_Biotic = @idAnti_Biotic
END

select * from Anti_Biotic
EXEC delete_Anti_Biotic 6
select * from Anti_Biotic


select * from Anti_Biotic

select dbo.TestAnti_Biotic(7,'Nurofen') as Rezultat

--Crud Anti Biotic
CREATE or alter PROCEDURE CRUD_Anti_Biotic @idAnti_Biotic int, @Nume VARCHAR(50), @Data_Expirare date, @nrOfRows INT AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @idAnti_Biotic2 int
	DECLARE @Nume2 VARCHAR(50)
	DECLARE @Data_Expirare2 date

	SET @idAnti_Biotic2=@idAnti_Biotic+100
	SET @Nume2 = @Nume + '1'
	SET @Data_Expirare2 = @Data_Expirare
	--test nume pasager
	IF(dbo.TestAnti_Biotic(@idAnti_Biotic, @Nume) = 1)
		BEGIN
			--CREATE= INSERT
			EXEC insert_Anti_Biotic @idAnti_Biotic, @Nume, @Data_Expirare, @nrOfRows
			--READ= SELECT
			SELECT * FROM Anti_Biotic
			--UPDATE= UPDATE
			EXEC update_Anti_Biotic @idAnti_Biotic, @Nume, @Data_Expirare,  @idAnti_Biotic2, @Nume2, @Data_Expirare2
			SELECT * FROM Anti_Biotic
			--DELETE= DELETE
			EXEC delete_Anti_Biotic @idAnti_Biotic2
			SELECT * FROM Anti_Biotic
			PRINT 'CRUD Operations on table Anti Biotic'
		END
		ELSE
		BEGIN
			PRINT 'Eroare de validare!'
			RETURN; 
		END
END

select * from Anti_Biotic
exec CRUD_Anti_Biotic 32, 'Nurofen', '2020-03-14', 10
select * from Anti_Biotic


----------------------viewuri si indexes-------------
--SELECT * FROM Articol
Select * From Medicamente

--CREATE NONCLUSTERED INDEX N_idx_idprodus ON Articole(IDprodus);
create nonclustered index N_idx_idprodus ON Medicamente(idMedicament);

create or alter view lab05_view1 as
	select Nume, count(*) as NrVariante
	from Medicamente
	group by Nume
go

select * from lab05_view1
------------------------------------------------------
SELECT * FROM Anti_Biotic

CREATE NONCLUSTERED INDEX N_idx_DataCIN ON Anti_Biotic(Data_Expirare);

create or alter view lab05_view2 as
	select * from Anti_Biotic
	where MONTH(Data_Expirare)=MONTH(GETDATE()) and year(Data_Expirare)=year(GETDATE())

select * from lab05_view2
