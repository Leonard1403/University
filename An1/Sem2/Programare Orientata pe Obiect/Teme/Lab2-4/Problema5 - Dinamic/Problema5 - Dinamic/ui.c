#pragma once
#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>
#include <stdio.h>

#include "my_utils.h"
#include "service.h"

void testAll()
{
	testAddService();
	testCopy();

	//testDelete();

	testCreateDelete();
	testCreateVector();

	testDeleteService();
	testFilterService();
	testFindService();
	testModifyService();

	testIterate();
	testValideaza();

	testCMP();
	testsortTranzactii();
}
void Default(MyList* v)
{
	int da;
	da = addTranzactie(v, 19, 6000, "iesire", "Youtube Premium");
	da = addTranzactie(v, 12, 200, "intrare", "Full masina");
	//assert(da == 1);
	da = addTranzactie(v, 20, 15, "iesire", "Tips");
	//assert(da == 1);
	da = addTranzactie(v, 19, 6000, "intrare", "alimentare");
	da = addTranzactie(v, 19, 500, "iesire", "magazie");
	//assert(da == 1);
	//destroy(&newList);
}

void printAllTranzactii(MyList* v)
{
	if (v->length == 0)
	{
		printf("Nu exista tranzactii. \n");
	}
	else
	{
		printf("Tranzactiile curente sunt:\n");
		for (int i = 0; i < size(v); i++)
		{
			Tranzactie m = get(v, i);
			printf("Ziua: %d | Suma: %d | Tip: %s | Descrierea: %s\n", m.ziua, m.suma, m.tip, m.descriere);
		};
	};
}

void printMenu()
{
	printf("1. Adauga tranzactie\n2. Modificare tranzactie existenta\n");
	printf("3. Stergere tranzactie existenta\n4. Vizualizare tranzactii dupa un criteriu(tip,suma>filtru)\n");
	printf("5. Vizualizare tranzactii ordonat dupa suma sau zi\n6. Vizualizare lista.\n");
	printf("0. Iesire din aplicatie.\n");
}

void uiAdd(MyList* v)
{
	char tip[30], descriere[300];
	int suma, ziua;
	char temp;
	scanf_s("%c", &temp, 1);
	printf("Ziua tranzactiei este: ");
	scanf_s("%d", &ziua);
	printf("Suma tranzactiei este: ");
	scanf_s("%d", &suma);
	scanf_s("%c", &temp, 1);
	printf("Tipul tranzactiei este: ");
	fgets(tip, 30, stdin);
	printf("Descriere tranzactiei este: ");
	fgets(descriere, 300, stdin);
	trimTrailing(tip);
	trimTrailing(descriere);
	//printf("%d | %d | %s | %s\n", ziua, suma, tip, descriere);
	int succesful = addTranzactie(v, ziua, suma, tip, descriere);
	if (succesful)
	{
		printf("Tranzactia a fost contorizata cu succes.\n");
	}
	else
	{
		printf("Tranzactie invalida\n");
	}
}

void uiModify(MyList* v)
{
	char tip[30];
	int sumanoua, ziua;
	char temp;
	scanf_s("%c", &temp, 1);
	printf("Ziua tranzactiei este: ");
	scanf_s("%d", &ziua);
	printf("Noua suma tranzactiei este: ");
	scanf_s("%d", &sumanoua);
	scanf_s("%c", &temp, 1);
	printf("Tipul tranzactiei este: ");
	fgets(tip, 30, stdin);
	//printf("Descriere tranzactiei este: ");
	//fgets(descriere, 300, stdin);
	trimTrailing(tip);
	//trimTrailing(descriere);
	//printf("%d | %d | %s | %s\n", sumanoua, ziua, tip, descriere);
	int succesful = modifyTranzactie(v, ziua, sumanoua, tip);
	if (succesful)
		printf("Tranzactia a fost modificata cu succes.\n");
	else
		printf("Nu exista tranzactie cu datele astea.\n");
}

void uiDelete(MyList* v) {
	int ziua;

	printf("Ziua in care s-a efectuat tranzactia: ");
	scanf_s("%d", &ziua);
	//printf("%d\n", ziua);
	int successful = deleteTranzactie(v, ziua);
	if (successful)
		printf("Tranzactia a fost stearsa cu succes.\n");
	else
		printf("Nu exista tranzactie in ziua respectiva.\n");
}

void uiFilter(MyList* v)
{
	char tip[30];
	int suma, ok;
	char temp;

	printf("Suma pentru care doriti filtru: ");
	scanf_s("%d", &suma);
	scanf_s("%c", &temp, 1);
	printf("Tipul pentru care doriti filtru: ");
	fgets(tip, 30, stdin);
	printf("Filtrul dupa suma mai mica sau mai mare(0/1): ");
	scanf_s("%d", &ok);

	trimTrailing(tip);

	//printf("%s\n", tip);
	MyList filteredList = filterTranzactii(v, tip, suma, ok);
	printAllTranzactii(&filteredList);
	destroy(&filteredList);
}

void uiSort(MyList* v)
{
	int rev;
	printf("Ordonare crescator sau descrescator(0/1)?:");
	scanf_s("%d", &rev);
	MyList sorted = sortTranzactii(v, rev,CMP_ZIUA_SUMA);
	printAllTranzactii(&sorted);
	destroy(&sorted);
}

void run()
{
	MyList tranzactiiList = createEmpty();
	Default(&tranzactiiList);
	int running = 1;
	while (running)
	{
		printMenu();
		int cmd;
		printf("Comanda este:");
		scanf_s("%d", &cmd);
		switch (cmd) {
		case 1:
			uiAdd(&tranzactiiList);
			break;
		case 2:
			uiModify(&tranzactiiList);
			break;
		case 3:
			uiDelete(&tranzactiiList);
			break;
		case 4:
			uiFilter(&tranzactiiList);
			break;
		case 5:
			uiSort(&tranzactiiList);
			break;
		case 6:
			printAllTranzactii(&tranzactiiList);
			break;
		case 0:
			running = 0;
			destroy(&tranzactiiList);
			break;
		default:
			printf("Comanda invalida\n");
		}
	}
}
int main()
{
	testAll();
	run();
	_CrtDumpMemoryLeaks();
	return 0;
}