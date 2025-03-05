use Farmacie 
go

-- Creare procedurã stocatã Deadlock_T1
CREATE OR ALTER PROCEDURE Deadlock_T1 AS
BEGIN
    BEGIN TRAN
    BEGIN TRY
        UPDATE Comenzi 
        SET Data_Livrare = DATEADD(DAY, -1, GETDATE()) -- Modificarea datelor comenzilor pentru a crea un deadlock
        WHERE Data_Livrare < GETDATE();

        INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Comenzi', CURRENT_TIMESTAMP);

        WAITFOR DELAY '00:00:10';

        UPDATE Clienti 
        SET Nume = 'John Doe T1' -- Modificarea datelor clientilor pentru a crea un deadlock
        WHERE idClient IN (
            SELECT idClient 
            FROM Comenzi 
            WHERE Data_Livrare < GETDATE()
        );

        INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Clienti', CURRENT_TIMESTAMP);

        COMMIT TRAN;
        SELECT 'Transaction committed' AS [Message];
    END TRY
    BEGIN CATCH
        ROLLBACK TRAN;
        SELECT 'Transaction rollbacked' AS [Message];
    END CATCH;
END;

EXECUTE Deadlock_T1;

-- Creare procedurã stocatã Deadlock_T1_C#
GO
CREATE OR ALTER PROCEDURE Deadlock_T1_C# AS
BEGIN
    BEGIN TRAN
    UPDATE Clienti 
    SET Nume = 'Jane DoeT1' -- Modificarea datelor clientilor pentru a crea un deadlock
    WHERE idClient IN (
        SELECT idClient 
        FROM Comenzi 
        WHERE Data_Livrare < GETDATE()
    );

    INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Clienti', CURRENT_TIMESTAMP);

    WAITFOR DELAY '00:00:05';

    UPDATE Comenzi 
    SET Data_Livrare = DATEADD(DAY, -1, GETDATE()) -- Modificarea datelor comenzilor pentru a crea un deadlock
    WHERE Data_Livrare < GETDATE();

    INSERT INTO LogTable(operatia, tabel, timpul) VALUES ('UPDATE', 'Comenzi', CURRENT_TIMESTAMP);

    COMMIT TRAN;
    SELECT 'Transaction committed' AS [Message];
END;

EXECUTE Deadlock_T1_C#;