#pragma once
#include "MyList.h"

/*
* Adauga o Tranzactie
*
* @param v: (adresa pentru) lista in care se adauga (MyList* v)
* @param ziua: ziua in care se face tranzactia(int)
* @param suma: suma care urmeaza sa fie transferata(int)
* @param tip: tipul sumei(de intrare sau iesire) (char*)
* @param descriere: descrierea tranzactiei
*
* @return: 1 daca tranzactia a fost adaugata cu succes, 0 altfel (int)
* post: tranzactia cu datele date este adaugata in lista (daca este o tranzactie valida)
*/

int addTranzactie(MyList* v, int ziua, int suma, char* tip, char* descriere);




/*
* Sterge o tranzactie
*
* @param v: (adresa pentru) lista din care se sterge (MyList* v)
* @param ziua: ziua pentru care se sterge tranzactia(int)
*
* @return: 1 daca tranzactia a fost stearsa cu succes, 0 altfel (int)
* post: tranzactia cu ziua, suma si tipul dat este stearsa din lista daca exista
*/
int deleteTranzactie(MyList* v, int ziua);




/*
* Modifica o tranzactie
*
* @param v: (adresa pentru) lista in care se modifica (MyList* v)
* @param ziua: ziua pentru care se modifica tranzactia(int)
* @param suma: noua suma pentru care se modifica tranzactia(int)
* @param tip:  noul tip sumei(de intrare sau iesire) pentru care se modifica tranzactia (char*)
*
* @return: 1 daca tranzactia a fost modificata cu succes, 0 altfel (int)
* post: tranzactia cu ziua, suma noua si tipul (daca o astfel
*		de tranzactie exista)
*/
int modifyTranzactie(MyList* v, int ziua, int sumaNoua, char* tip, char* descriere);





/*
* Gaseste o tranzactie cu ziua si suma data
*
* @param v: (adresa pentru) lista in care se cauta (MyList* v)
* @param ziua: ziua pentru care se cauta tranzactia(int)
*
* @return: pozitia din lista a tranzactiei cautate, -1 daca
			tranzactia nu exista in lista (int)
*/
int findTranzactie(MyList* v, int ziua);





/*
* Filtreaza lista de melodii dupa un artist dat
*
* @param v: (adresa pentru) lista data (MyList* v)
* @param tip: tipul dupa care se filtreaza lista(int)
* @param suma: suma dupa care se filtreaza lista(int)
* @param ok: parametru dupa care se va filtra lista in functie de suma mai mica sau mai mare
* @return: lista cu tranzactii care au tipul tip (MyList)
*/
MyList filterTranzactii(MyList* v, char* tip, int suma, int ok);





/*
* Returneaza o lista sortata de melodii
* Criteriu de sortare: durata (ascendent)
*
* @param v: (adresa pentru) lista data (MyList* v)
*
* @return: o lista sortata de melodii  (MyList)
*/
//MyList sortMelodii(MyList* v);

void testAddService();
void testModifyService();
void testDeleteService();
void testFindService();
void testFilterService();
//void testSortService();

