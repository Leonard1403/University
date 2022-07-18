#pragma once
#include <stdio.h>
#include "service.h"
#include <assert.h>
#include <string.h>
int addTranzactie(MyList* v, int ziua, int suma, char* tip, char* descriere)
{
	//printf("Intrat!\n");
	Tranzactie m = createTranzactie(ziua,suma,tip,descriere);
	//printf("Trecut creare\n");
	int successful = valideazaTranzactie(m);
	//printf("Trecut validare\n");
	//printf("succesful: %d",successful);
	if (!successful)
		return 0;
	add(v, m);
	return 1;
}

int findTranzactie(MyList* v, int ziua)
{
	int poz_to_delete = -1;
	for (int i = 0; i < v->length; i++) {
		Tranzactie m = get(v, i);
		//printf("ziua: %d\n", m.ziua);
		if (m.ziua == ziua) {
			poz_to_delete = i;
			break;
		}
	}
	return poz_to_delete;
}


int deleteTranzactie(MyList* v, int ziua)
{
	//printf("ziua: %d\n", ziua);
	int poz_to_delete = findTranzactie(v, ziua);
	if (poz_to_delete != -1) {
		Tranzactie m = delete(v, poz_to_delete);
		destroyTranzactie(&m);
		return 1;
	}
	else
		return 0;
}

int modifyTranzactie(MyList* v, int ziua, int sumaNoua, char* tip, char* descriere)
{
	int poz_to_delete = findTranzactie(v, ziua);

	if (poz_to_delete != -1) {
		Tranzactie tranzactieNoua = createTranzactie(ziua,sumaNoua,tip,descriere);
		Tranzactie m = get(v, poz_to_delete);
		destroyTranzactie(&m);
		setElem(v, poz_to_delete, tranzactieNoua);
		return 1;
	}
	else
		return 0;
}

MyList filterTranzactii(MyList* v, char* tip, int suma, int ok)
{
	//ok == 0 , atunci lista se va face dupa tranzactile cu suma mai mica decat cea data
	//ok == 1 , atunci lista se va face dupa tranzactile cu suma mai mare decat cea data
	MyList filteredList = createEmpty();
	//printf("Tipul din functia de tranzactii: %s\n", tip);
	if (strcmp(tip, "") != 0) {
		for (int i = 0; i < v->length; i++) {
			Tranzactie m = get(v, i);
			if (ok == 0) {
				if (strcmp(tip, m.tip) == 0 && suma > m.suma) {
					//printf("OK = %d, Tipul = %s", ok, tip);
					add(&filteredList, createTranzactie(m.ziua, m.suma, m.tip, m.descriere));
				}
			}
			else if (ok == 1)
			{
				if (strcmp(tip, m.tip) == 0 && suma < m.suma) {
					//printf("OK = %d, Tipul = %s", ok, tip);
					add(&filteredList, createTranzactie(m.ziua, m.suma, m.tip, m.descriere));
				}
			}
		}
		return filteredList;
	}
	else {
		return copyList(v);
	}

}


void testAddService() {
	MyList v = createEmpty();

	int successful1 = addTranzactie(&v,12,200,"intrare","Full masina");
	assert(successful1 == 1);

	int successful2 = addTranzactie(&v, 0, 0,"","");
	assert(successful2 == 0);

	int successful3 = addTranzactie(&v, 0, 15, "iesire", "Tips");
	assert(successful3 == 0);

	assert(size(&v) == 1);
	Tranzactie m = get(&v, 0);

	destroy(&v);


}

void testFindService() {
	MyList v = createEmpty();

	int successful1 = addTranzactie(&v, 15, 200, "intrare", "da");
	assert(successful1 == 1);

	int successful2 = addTranzactie(&v, 16, 202, "iesire", "da");
	assert(successful2 == 1);

	int successful3 = addTranzactie(&v, 17, 201, "intrare", "da");
	assert(successful3 == 1);

	assert(size(&v) == 3);
	int poz = findTranzactie(&v,16);

	assert(poz == 1);

	destroy(&v);
	assert(size(&v) == 0);
}

void testModifyService() {
	MyList v = createEmpty();

	int successful1 = addTranzactie(&v, 15, 200, "intrare", "da");
	assert(successful1 == 1);

	int successful2 = addTranzactie(&v, 16, 202, "iesire", "da");
	assert(successful2 == 1);

	int successful3 = addTranzactie(&v, 17, 201, "intrare", "da");
	assert(successful3 == 1);

	assert(size(&v) == 3);
	int modify_success = modifyTranzactie(&v, 15, 210, "intrare", "da");
	assert(modify_success == 1);
	int modify_success2 = modifyTranzactie(&v, 20, 99, "iesire", "da");
	assert(modify_success2 == 0);
	destroy(&v);
}

void testDeleteService() {
	MyList v = createEmpty();

	int successful1 = addTranzactie(&v, 15, 200, "intrare", "da");
	assert(successful1 == 1);

	int successful2 = addTranzactie(&v, 18, 200, "iesire", "masina");
	assert(successful2 == 1);

	int successful3 = addTranzactie(&v, 19, 6000, "intrare", "alimentare");
	assert(successful3 == 1);

	assert(size(&v) == 3);
	int succesful_del = deleteTranzactie(&v,15);
	assert(succesful_del == 1);
	int succesfully_del = deleteTranzactie(&v,20);
	assert(succesfully_del == 0);
	destroy(&v);
	assert(size(&v) == 0);
}

void testFilterService() {
	MyList v = createEmpty();

	int successful1 = addTranzactie(&v, 15, 200, "intrare", "da");
	assert(successful1 == 1);

	int successful2 = addTranzactie(&v, 18, 200, "iesire", "masina");
	assert(successful2 == 1);

	int successful3 = addTranzactie(&v, 19, 6000, "intrare", "alimentare");
	assert(successful3 == 1);


	assert(size(&v) == 3);

	MyList filteredList = filterTranzactii(&v,"intrare",6001,0);
	assert(size(&filteredList) == 2);
	destroy(&filteredList);

	filteredList = filterTranzactii(&v, "intrare", 100,1);
	//printf("size(filteredList) = %d\n", size(&filteredList));
	assert(size(&filteredList) == 2);
	
	filteredList = filterTranzactii(&v, "",200,1);
	//printf("size(filteredList) = %d\n", size(&filteredList));
	assert(size(&filteredList) == 3);
	destroy(&filteredList);

	destroy(&v);

}

//void testSortService() {
//	MyList v = createEmpty();
//
//	int successful1 = addMelodie(&v, "Child in Time", "Deep Purple", 59);
//	assert(successful1 == 1);
//
//	int successful2 = addMelodie(&v, "Kashmir", "Led Zeppelin", 56);
//	assert(successful2 == 1);
//
//	int successful4 = addMelodie(&v, "When The Levee Breaks", "Led Zeppelin", 58);
//	assert(successful4 == 1);
//
//	int successful3 = addMelodie(&v, "(Don't fear) The Reaper", "Blue Oyster Cult", 76);
//	assert(successful3 == 1);
//
//	assert(size(&v) == 4);
//	MyList sortedList = sortMelodii(&v);
//	assert(get(&sortedList, 0).durata == 56);
//	assert(get(&sortedList, 1).durata == 58);
//	assert(get(&sortedList, 2).durata == 59);
//	assert(get(&sortedList, 3).durata == 76);
//
//
//	destroy(&sortedList);
//	destroy(&v);
//}