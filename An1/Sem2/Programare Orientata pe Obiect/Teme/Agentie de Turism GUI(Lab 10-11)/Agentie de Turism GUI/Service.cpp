#pragma once
#include "Service.h"
#include <assert.h>
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <exception>

using std::sort;

void TurismStore::addTurism(string denumire, string destinatie, string tip, int pret) {
	Turism s1{ denumire,destinatie,tip,pret };
	val.valideaza(s1);
	repo.store(s1);
	undoActions.push_back(std::make_unique<UndoAdd>(repo, s1));
}

void TurismStore::stergereTurism(string denumire) {
	Turism s = repo.find(denumire);
	repo.sterge(s);
	undoActions.push_back(std::make_unique<UndoDelete>(repo, s));
}

void TurismStore::modifyTurism(string denumire, string destinatie, string tip, int pret) {
	Turism a{ denumire,destinatie,tip,pret };
	val.valideaza(a);
	undoActions.push_back(std::make_unique<UndoModify>(repo, a, repo.find(denumire)));
	repo.modify(a);
}

/*
void TurismStore::deleteTurism(string denumire, string destinatie, string tip) {
	//repo.find(denumire, destinatie, tip);
}

void TurismStore::modifyTurism(string denumire, string destinatie, string tip) {
	//repo.find(denumire, destinatie, tip);
}
*/

void TurismStore::undo() {
	if (undoActions.empty())
		throw std::exception();

	undoActions.back()->doUndo();
	undoActions.pop_back();
}

Turism TurismStore::search(string denumire) {
	return repo.find(denumire);
}

vector <Turism> TurismStore::generalSort(bool(*Function)(const Turism&, const Turism&)) {
	vector <Turism> v{ repo.getAllTurism() };

	for (size_t i = 0; i < v.size(); i++) {
		for (size_t j = i + 1; j < v.size(); j++) {
			if (!Function(v[i], v[j])) {
				Turism aux = v[i];
				v[i] = v[j];
				v[j] = aux;
			}
		}
	}

	return v;
}

vector <Turism> TurismStore::sortByDenumire() {
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpDenumire);
	return sortedCopy;
}

vector <Turism> TurismStore::sortByDestinatie() {
	/*
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpDestinatie);
	return sortedCopy;
	*/
	return generalSort(cmpDestinatie);
}

vector <Turism> TurismStore::sortByTipAndPret() {
	auto sortedCopy = repo.getAllTurism();
	sort(sortedCopy.begin(), sortedCopy.end(), cmpTipAndPret);
	return sortedCopy;
}

vector <Turism> TurismStore::filter(function<bool(const Turism&)> fct) {
	vector <Turism> filteredTurism;
	for (const auto& turist : repo.getAllTurism()) {
		if (fct(turist)) {
			filteredTurism.push_back(turist);
		}
	}
	return filteredTurism;
}

vector <Turism> TurismStore::filtrareDestinatie(string destinatie) {
	return filter([destinatie](const Turism& m) {
		return m.getDestinatie() == destinatie;
		});
}

vector <Turism> TurismStore::filtrarePret(int pret) {
	return filter([pret](const Turism& m) {
		return m.getPret() == pret;
	});
}

size_t TurismStore::getSizeOfTurism() {
	return repo.get_dim();
}

//WISHLIST

void TurismStore::storeWishlist(std::string denumire) {
	Turism a = repo.find(denumire);
	wishlist.valideaza_turism(a);
	wishlist.adauga_wishlist(a);
}

size_t TurismStore::storeRandom(int n) {
	wishlist.adauga_random(this->repo.getAllTurism(), n);
	return wishlist.get_all_from_wishlist().size();
}

void TurismStore::golesteWishlist() {
	wishlist.goleste_wishlist();
}

const vector<Turism>& TurismStore::getAllWishlist() {
	return wishlist.get_all_from_wishlist();
}

//Fisiere
void TurismStore::saveWishlistToFile(std::string fileName){
	std::ofstream out(fileName);
	if (!out.is_open()) {
		//throw RepoException("Fisierul nu se poate deschide!");
	}
	for (auto& activity : getAllWishlist()) {
		out << activity.getDenumire() << ";" << activity.getDestinatie() << ";" << activity.getTip() << ";" << activity.getPret() << std::endl;
	}
	out.close();
}

size_t TurismStore::getSizeOfWishlist() {
	return getAllWishlist().size();
}

//TESTE	

void testModifyTurism()
{
	TurismRepository test_repo;
	TurismValidator test_val;
	Wishlist wishlist;
	TurismStore test_srv{ test_repo,test_val,wishlist };
	test_srv.addTurism("Denumire", "Destinatie", "Tip",200);
	test_srv.modifyTurism("Denumire", "Destinatie", "Tip", 2000);
}

void teststoreRandom() {
	TurismRepositoryFile test_repo{ "E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test.txt" };
	TurismValidator test_val;
	Wishlist wishlist;
	TurismStore test_srv{ test_repo,test_val,wishlist };
	test_srv.storeRandom(2);
}

void test_save_to_file_srv() {
	TurismRepositoryFile test_repo{ "E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test.txt" };
	TurismValidator test_val;
	Wishlist wishlist;
	TurismStore test_srv{ test_repo,test_val,wishlist };

	test_srv.addTurism("La munte", "Sinaia", "munte", 200);
	test_srv.storeWishlist("La munte");

	test_srv.saveWishlistToFile("E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test_program.txt");

	std::ifstream in("E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test_program.txt");
	std::string line;
	while (getline(in, line)) {
		std::string denumire, destinatie;
		std::stringstream linestream(line);
		std::string current_item;
		int no = 0;
		while (std::getline(linestream, current_item, ';')) {
			if (no == 0)
				denumire = current_item;
			if (no == 1)
				destinatie = current_item;
			no++;
		}

		assert(denumire == "La munte");
		assert(destinatie == "Sinaia");
	}
	in.close();

	test_srv.golesteWishlist();
	test_srv.saveWishlistToFile("E:\\Facultate\\An1\\Sem2\\Programare orientata pe obiect\\Teme\\Agentie de turism\\Problema 6\\Problema 6\\test_program.txt");

	test_srv.stergereTurism("La munte");
}

void testAddService() {
	TurismRepository testRepo;
	TurismValidator testVal;
	Wishlist wishlist;
	TurismStore testService{ testRepo,testVal, wishlist };

	testService.addTurism("La munte","Sinaia","munte",200);
	testService.addTurism("La poiana","Brasov","munte",200);
	assert(testService.getAllTurism().size() == 2);

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
	Wishlist wishlist;
	TurismStore testService{ testRepo, testVal, wishlist };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	vector <Turism> oferte = testService.filtrareDestinatie("Floresti");
	assert(oferte.size() == 2);

	vector <Turism> oferte2 = testService.filtrarePret(500);
	assert(oferte.size() == 2);
}

void testSortService() {
	TurismRepository testRepo;
	TurismValidator testVal;
	Wishlist wishlist;
	TurismStore testService{ testRepo, testVal, wishlist };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);
	
	//sortByDenumire
	//sortByDestinatie
	//sortByTipAndPret

	vector <Turism> sortByDenumire = testService.sortByDenumire();
	assert(sortByDenumire[0].getDenumire() == "Belvedere");

	vector <Turism> sortByDestinatie = testService.sortByDestinatie();
	assert(sortByDestinatie[0].getDestinatie() == "Cluj-Napoca");

	vector <Turism> sortByTipAndPret = testService.sortByTipAndPret();
}

void testSearch() {
	TurismRepository testRepo;
	TurismValidator testVal;
	Wishlist wishlist;
	TurismStore testService{ testRepo, testVal, wishlist };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	try {
		testService.search("Laprapastia din vale");
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
	Wishlist wishlist;
	TurismStore testService{ testRepo, testVal, wishlist };

	//Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	//Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	//Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };

	testService.addTurism("La prapastia din vale", "Floresti", "munte", 200);
	testService.addTurism("La Veriku", "Cluj-Napoca", "atelier auto", 500);
	testService.addTurism("Belvedere", "Cluj-Napoca", "hotel", 500);
	testService.addTurism("La prapastia din deal", "Floresti", "munte", 9800);

	testService.stergereTurism("La prapastia din vale");

}

void testService() {
	testFilterService();
	testSearch();
	testAddService();
	testFilterService();
	testSortService();
	teststergereTurism();
	teststoreRandom();

	test_save_to_file_srv();
	teste_wishlist();
	testModifyTurism();
}


