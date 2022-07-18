#pragma once
#include "Repository.h"
#include "validators.h"
#include <functional>

using std::function;

class TurismStore {
private:
	TurismRepository& repo;
	TurismValidator& val;

	vector<Turism> filter(function<bool(const Turism&)> fct);

	vector<Turism> generalSort(bool(*Function)(const Turism&, const Turism&));

public:
	TurismStore(TurismRepository& turismRepo, TurismValidator& val) :repo{ turismRepo }, val{ val }{};
	TurismStore(const TurismStore& ot) = delete;

	/*
	* Adauga o o locatie de turism dupa denumire, destinatie, tip, pret
	* @throws:
	* RepoException daca mai exista locatie de turism cu destinatia si tipul dat
	* ValidationException daca locatia turism nu este valida
	*/
	void addTurism(string denumire, string destinate, string tip, int pret);
	void stergereTurism(string denumire, string destinatie, string tip);
	
	//void deleteTurism(string denumire, string destinatie, string tip);
	//void modifyTurism(string denumire, string destinatie, string tip);

	Turism search(string denumire, string destinatie, string tip);

	const vector<Turism>& getAllTurism() {
		return this->repo.getAllTurism();
	}
	// sortare oferte dupa: denumire, destinatie, tip + pret
	//void cautareTurism(string tip);
	//filtrare oferte turistice dupa: destinatie, pret
	
	vector <Turism> filtrareDestinatie(string destinatie);
	vector <Turism> filtrarePret(int pret);

	vector <Turism> sortByDenumire();
	vector <Turism> sortByDestinatie();
	vector <Turism> sortByTipAndPret();
};

void testAddService();
void testService();