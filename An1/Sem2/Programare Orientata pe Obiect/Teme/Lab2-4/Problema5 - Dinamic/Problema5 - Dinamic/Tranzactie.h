#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

typedef struct {
	char* tip;
	char* descriere;

	int ziua;
	int suma;


} Tranzactie;

/*
* Creeaza un nou cont bancar
*
* @param ziua:		Ziua din luna in care s-a efectuat tranzactia
* @param suma:		Suma tranzactionata
* @param tipul:		Tipul tranzactiei(intrare/iesire)
* @param descriere:	Descrierea tranzactiei
*
* @return Tranzactia creata
*/

Tranzactie createTranzactie(int ziua, int suma, char* tip, char* descriere);

/*
* Sterge tranzactie
*/

void destroyTranzactie(Tranzactie* m);
/*
* Validarea tranzactilor
* O tranzactie este valida daca
* suma > 0
* ziua = [1,31]
* tipul = {intrare,iesire}
* @param m: Tranzactia pentru validare (Tranzactie)
* 
* @return: 1 daca tranzactia este valida, 0 daca nu este valida
*/

int valideazaTranzactie(Tranzactie m);

Tranzactie copyTranzactie(Tranzactie m);

void testCreateDelete();
void testValideaza();