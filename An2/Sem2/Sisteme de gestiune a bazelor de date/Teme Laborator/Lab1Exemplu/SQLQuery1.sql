create database DBSolisti
go
use DBSolisti
go
create table CasaDiscuri(
codCD int primary key identity(1,1),
Nume varchar(50)
)

--drop table Solist

create table Solist(
CodS int primary key identity(1,1),
Nume varchar(50),
Varsta int,
codCD int foreign key references CasaDiscuri(codCD)
)
select * from CasaDiscuri
select * from Solist
insert into CasaDiscuri values ('casa 1'), ('casa 2')
insert into Solist values ('bon jovi', 54,1), ('guns un roses', 45, 2)