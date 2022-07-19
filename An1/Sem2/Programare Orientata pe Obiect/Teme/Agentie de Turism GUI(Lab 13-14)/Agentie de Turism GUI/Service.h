#pragma once
#include "Repository.h"
#include "undo.h"
#include "Wishlist.h"
#include "validators.h"
#include <functional>
#include <vector>

using std::function;
using std::vector;

class TurismStore {
private:
	TurismRepository& repo;
	TurismValidator& val;
	Wishlist& wishlist;

	vector < unique_ptr <ActiuneUndo>> undoActions;

	vector<Turism> filter(function<bool(const Turism&)> fct);

	vector<Turism> generalSort(bool(*Function)(const Turism&, const Turism&));

public:
	TurismStore(TurismRepository& turismRepo, TurismValidator& val, Wishlist& wishlist) :repo{ turismRepo }, val{ val }, wishlist{wishlist}{};
	TurismStore(const TurismStore& ot) = delete;

	/*
	* Adauga o o locatie de turism dupa denumire, destinatie, tip, pret
	* @throws:
	* RepoException daca mai exista locatie de turism cu destinatia si tipul dat
	* ValidationException daca locatia turism nu este valida
	*/
	void addTurism(string denumire, string destinate, string tip, int pret);
	void stergereTurism(string denumire);
	void modifyTurism(string denumire, string destinate, string tip, int pret);
	
	//void deleteTurism(string denumire, string destinatie, string tip);
	//void modifyTurism(string denumire, string destinatie, string tip);

	Turism search(string denumire);

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

	size_t getSizeOfTurism();

	void undo();

	//Wishlist

	Wishlist& get_wishlist() {
		return this->wishlist;
	}
	void storeWishlist(string denumire);
	size_t storeRandom(int n);
	void golesteWishlist();

	const vector<Turism>& getAllWishlist();
	
	//File
	void saveWishlistToFile(string filename);
	
	size_t getSizeOfWishlist();

	vector <Turism> loadWishlistFromFile(std::string filename);
};

void testAddService();
void testService();