use Farmacie
go
/*1 - Pentru fiecare Comanda se va afisa Clientul*/

Select C.Nume, C.varsta, M.numeComenzi,M.Data_Livrare
From Clienti C, Comenzi M
where C.idClient = M.idClient

/*2 - Pentru fiecare Medicament se va afisa Clientul*/

Select C.Nume , M.Nume
From Clienti C , Medicamente M
where C.idClient = M.idClient

/*3- Cate inregistrari de pastile pentru clienti avem din fiecare*/

Select M.Nume , COUNT(M.idMedicament)
From Clienti C, Medicamente M
Where M.idClient = C.idClient
Group by M.Nume

/*4 - Interogarile pentru care clientii care au 3 seturi de pastile*/

Select C.Nume,  count(M.Nume)
From Clienti C, Medicamente M
where M.idClient = C.idClient
Group by C.nume
Having Count(C.Nume)  = 3

/*5 - Se afiseaza toate medicamentele care sunt anti-biotic*/

Select Anti_Biotic.Nume, Anti_Biotic.Data_Expirare, Medicamente.Pret 
From Medicamente
Inner Join Anti_Biotic_Medicamente
ON Medicamente.idMedicament = Anti_Biotic_Medicamente.idMedicament
Inner Join Anti_Biotic
ON Anti_Biotic_Medicamente.idAnti_Biotic = Anti_Biotic.idAnti_Biotic

/*6 - 5 dar cu having*/
Select A1.Nume, A1.Data_Expirare, M.Pret
From Anti_Biotic A1, Medicamente M, Anti_Biotic_Medicamente A2
Where A1.idAnti_Biotic = A2.idAnti_Biotic and A2.idMedicament = M.idMedicament

/*7 - Se afiseaza toate medicamentele predestinate clientilor o singura data*/
Select Distinct M.nume
/*Select **/
From Clienti C, Medicamente M
where C.idClient = M.idClient

/*8- Se afiseaza numarul total de medicamente pe care le-au luat clientii*/
Select count(Distinct M.nume)
From Medicamente M, Clienti C
where M.idClient  = C.idClient

/*9- Toate medicamentele care incep cu A*/
Select M.Nume
From Medicamente M
Group by M.Nume
Having M.nume Like 'A%'

/*10- Se afiseaza managerul*/

Select M.Nume
From Manager M, Angajati A
Where M.idManager = A.idManager

/*11 - Ce Medicamente are Managerul*/

Select M1.Nume, M3.Nume
From Manager M1, Angajati A1, Magazin M2, Clienti C1,Medicamente M3
Where M1.idManager = A1.idManager and A1.idAngajati=M2.idAngajati and M2.idClient=C1.idClient and C1.idClient = M3.idClient

/*12 - Ce medicamente are fiecare Angajat*/
Select A1.Nume, M3.Nume
From Manager M1, Angajati A1, Magazin M2, Clienti C1,Medicamente M3
Where A1.idAngajati=M2.idAngajati and M2.idClient=C1.idClient and C1.idClient = M3.idClient

/*13 - Se afiseaza toata medicamentele care sunt pentru alergii */
Select M.Nume
From Medicamente M, Alergii_Medicamente A1, Alergii A2
Where M.idMedicament = A1.idMedicament and A1.idAlergii = A2.idAlergii

Select C.Nume , M.Nume
From Clienti C, Medicamente M
where C.idClient = M.idClient

Select*
From Clienti
Select *
From Medicamente
Select *
From Alergii

/*14 - Numele Comenzii si medicamentul*/
Select C1.numeComenzi, M.Nume
From Comenzi C1, Clienti C2, Medicamente M
Where C1.idClient = C2.idClient and C2.idClient = M.idClient

/*15 - Managerul care este Client*/

Select M1.Nume, C1.varsta
From Manager M1, Angajati A1, Magazin M2, Clienti C1
Where M1.idManager = A1.idManager and A1.idAngajati = M2.idAngajati and M2.idClient = C1.idClient

/*16 - Clientul si Distribuitorul */
Select C1.Nume, C1.varsta, D1.Nume
From Clienti C1, Medicamente M1, Medicamente_Distribuitori M2, Distribuitori D1 
where C1.idClient = M1.idClient and M1.idMedicament = M2.idMedicament and M2.idDistribuitor = D1.idDistribuitor
