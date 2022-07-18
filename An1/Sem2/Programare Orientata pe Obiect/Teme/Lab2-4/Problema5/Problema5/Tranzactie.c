#pragma once
#include "Tranzactie.h"
#include <string.h>
#include <assert.h>

Tranzactie createTranzactie(int ziua, int suma, char* tip, char* descriere)
{
	Tranzactie m;
	m.ziua = ziua;
	m.suma = suma;
	strcpy_s(m.tip,sizeof(m.tip),tip);
	strcpy_s(m.descriere, sizeof(m.descriere), descriere);
	//printf("%d | %d | %s | %s", m.ziua, m.suma, m.tip, m.descriere);
	return m;
}

void destroyTranzactie(Tranzactie* m)
{
	m->ziua = 0;
	m->suma = 0;
	m->tip[0] = '\0';
	m->descriere[0] = '\0';
}

int valideazaTranzactie(Tranzactie m)
{
	if (m.suma <= 0)
	{
		//printf("Suma nu este buna %d\n", m.suma);
		return 0;
	}
	if (m.ziua < 1 || m.ziua > 31)
	{
		//printf("Ziua nu este buna %s\n", m.ziua);
		return 0;
	}
	if (strcmp(m.tip, "intrare") != 0 && strcmp(m.tip, "iesire") != 0)
	{
		//printf("Tipul nu este buna %s\n", m.tip);
		return 0;
	}
	return 1;
}

void testCreateDelete()
{
	Tranzactie m = createTranzactie(14, 2000, "intrare", "O suma venerabila");

	assert(m.ziua == 14);
	assert(m.suma == 2000);
	assert(strcmp(m.tip, "intrare") == 0);
	assert(strcmp(m.descriere, "O suma venerabila") == 0);

	destroyTranzactie(&m);
	assert(m.ziua == 0);
	assert(m.suma == 0);
	assert(strlen(m.tip) == 0);
	assert(strlen(m.descriere) == 0);
}

void testValideaza()
{
	Tranzactie m1 = createTranzactie(0, 15, "intrare", "Taxa pentru youtube premium");
	assert(valideazaTranzactie(m1) == 0);
	Tranzactie m2 = createTranzactie(1, 0, "intrare", "Taxa pentru youtube premium");
	assert(valideazaTranzactie(m2) == 0);
	Tranzactie m3 = createTranzactie(1, 15, "ew", "Taxa pentru youtube premium");
	assert(valideazaTranzactie(m3) == 0);

	Tranzactie m4 = createTranzactie(1, 15, "intrare", "Taxa pentru youtube premium");
	assert(valideazaTranzactie(m4) == 1);
}