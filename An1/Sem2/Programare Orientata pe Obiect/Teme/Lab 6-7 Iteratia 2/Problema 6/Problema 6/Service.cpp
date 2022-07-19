#pragma once
#include "Service.h"
#include <assert.h>
#include <functional>
#include <algorithm>

using std::sort;

void TurismStore::addTurism(string denumire, string destinatie, string tip, int pret) {
	Turism s1{ denumire,destinatie,tip,pret };
	val.valideaza(s1);
	repo.store(s1);
}

void TurismStore::stergereTurism(string denumire, string destinatie, string tip) {
	Turism s = repo.find(denumire, destinatie, tip);
	repo.sterge(s);
}
/*
void TurismStore::deleteTurism(string denumire, string destinatie, string tip) {
	//repo.find(denumire, destinatie, tip);
}

void TurismStore::modifyTurism(string denumire, string destinatie, string tip) {
	//repo.find(denumire, destinatie, tip);
}
*/

Turism TurismStore::search(string denumire, string destinatie, string tip) {
	return repo.find(denumire, destinatie, tip);
}

VectorDinamic <Turism> TurismStore::generalSort(bool(*Function)(const Turism&, const Turism&)) {
	VectorDinamic <Turism> v{ repo.getAllTurism() };

	for (int i = 0; i < v.size(); i++) {
		for (int j = i + 1; j < v.size(); j++) {
			if (!Function(v[i], v[j])) {
				Turism aux = v[i];
				v[i] = v[j];
				v[j] = aux;
			}
		}
	}

	return v;
}

VectorDinamic <Turism> TurismStore::sortByDenumire() {
	/*
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpDenumire);
	return sortedCopy;
	*/
	return generalSort(cmpDenumire);
}
		
VectorDinamic <Turism> TurismStore::sortByDestinatie() {
	/*
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpDestinatie);
	return sortedCopy;
	*/
	return generalSort(cmpDestinatie);
}

VectorDinamic <Turism> TurismStore::sortByTipAndPret() {
	/*
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpTipAndPret);
	return sortedCopy;
	*/
	return generalSort(cmpTipAndPret);
}

VectorDinamic <Turism> TurismStore::filter(function<bool(const Turism&)> fct) {
	VectorDinamic <Turism> filteredTurism;

	
	VectorDinamic <Turism> allTuristi = repo.getAllTurism();
	for (int i = 0; i < allTuristi.size(); i++)
	{
		if (fct(allTuristi[i]))
		{
			filteredTurism.push_back(allTuristi[i]);
		}
	}
	
	/*
	for (const auto& turist : repo.getAllTurism()) {
		if (fct(turist)) {
			filteredTurism.push_back(turist);
		}
	}
	*/

	return filteredTurism;
}

VectorDinamic <Turism> TurismStore::filtrareDestinatie(string destinatie) {
	return filter([destinatie](const Turism& m) {
		return m.getDestinatie() == destinatie;
		});
}

VectorDinamic <Turism> TurismStore::filtrarePret(int pret) {
	return filter([pret](const Turism& m) {
		return m.getPret() == pret;
	});
}

void testAddService() {
	TurismRepository testRepo;
	TurismValidator testVal;
	TurismStore testService{ testRepo,testVal };

	testService.addTurism("La munte","Sinaia","munte",200);
	testService.addTurism("La poiana","Brasov","munte",200);
	
	VectorDinamic < Turism > allTuristi = testService.getAllTurism();
	
	assert(allTuristi.size() == 2);

	try {
		testService.addTurism("La munte", "Sinaia", "munte", 200);
		//modif ->
		//assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}

	//string denumire;
	//string destinatie;
	//string tip;
	//int pret;

	try {
		testService.addTurism("","Sinaia","munte",200);
		//modif ->
		//assert(false);
	}
	catch (ValidationException& ve) {
		assert(ve.getErrorMessages() == "Denumirea locatiei este prea scurta\n");
	}

	try {
		testService.addTurism("La munte", "Sinaia", "", 20);
		//modif ->
		//assert(false);
	}
	catch (ValidationException& ve) {
		assert(ve.getErrorMessages()== "Tipul locatiei trebuie sa fie mai lung decat 2\n");
	}

	try {
		testService.addTurism("La munte", "Sinaia", "da", 5);
		//modif ->
		//assert(false);
	}
	catch (ValidationException& ve) {
		assert(ve.getErrorMessages() == "Pretul locatiei de turism este de pomana\n");
	}

}

void testFilterService() {
	TurismRepository testRepo;
	TurismValidator testVal;
	TurismStore testService{ testRepo, testVal };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	VectorDinamic <Turism> oferte = testService.filtrareDestinatie("Floresti");
	assert(oferte.size() == 2);

	VectorDinamic <Turism> oferte2 = testService.filtrarePret(500);
	assert(oferte.size() == 2);
}

void testSortService() {
	TurismRepository testRepo;
	TurismValidator testVal;
	TurismStore testService{ testRepo, testVal };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);
	
	//sortByDenumire
	//sortByDestinatie
	//sortByTipAndPret

	VectorDinamic <Turism> sortByDenumire = testService.sortByDenumire();
	assert(sortByDenumire[0].getDenumire() == "Belvedere");

	VectorDinamic <Turism> sortByDestinatie = testService.sortByDestinatie();
	assert(sortByDestinatie[0].getDestinatie() == "Cluj-Napoca");

	VectorDinamic <Turism> sortByTipAndPret = testService.sortByTipAndPret();
}

void testSearch() {
	TurismRepository testRepo;
	TurismValidator testVal;
	TurismStore testService{ testRepo, testVal };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	try {
		testService.search("Laprapastia din vale", "Floresti", "munte");
		//modif ->
		//assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
	//testService.search("da", "da", "da");
}

void teststergereTurism() {
	TurismRepository testRepo;
	TurismValidator testVal;
	TurismStore testService{ testRepo, testVal };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	testService.stergereTurism("La prapastia din vale", "Floresti", "munte");

}

void testService() {
	testFilterService();
	testSearch();
	testAddService();
	testFilterService();
	testSortService();
	teststergereTurism();
}


