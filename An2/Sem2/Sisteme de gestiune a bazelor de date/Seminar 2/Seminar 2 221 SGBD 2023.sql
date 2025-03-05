CREATE DATABASE Seminar2SGBD2212023;
GO
USE Seminar2SGBD2212023;
CREATE TABLE Magazine
(cod_m INT PRIMARY KEY IDENTITY,
nume VARCHAR(100),
tip VARCHAR(100),
tara VARCHAR(100)
);
CREATE TABLE Jocuri
(cod_j INT PRIMARY KEY IDENTITY,
nume VARCHAR(100),
tip VARCHAR(100),
pret REAL,
producator VARCHAR(100),
cod_m INT FOREIGN KEY REFERENCES Magazine(cod_m)
);
INSERT INTO Magazine (nume, tip, tara) VALUES
('STEAM','online','US'),('G2A','online','US'),('Altex','fizic','Romania');
INSERT INTO Jocuri (nume, tip, pret, producator, cod_m) VALUES 
('CSGO','Shooter',0,'Valve',1),('GTA5','Shooter',30,'Rockstar Games',1),
('LOL','MOBA',0,'Riot',3),('RDR2','Shooter',60,'Rockstar Games',2),
('Forza Horizon','Racing',60,'Playground Games',2),
('StarCraft 2','Real Time Strategy',40,'Blizzard',3);
SELECT * FROM Magazine;
SELECT * FROM Jocuri;