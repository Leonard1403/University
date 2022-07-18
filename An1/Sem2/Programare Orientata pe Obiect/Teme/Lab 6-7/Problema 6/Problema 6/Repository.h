#pragma once
#include "Turism.h"
#include <vector>

using std::vector;

class RepoException {
private:
	string errorMsg;
public:
	RepoException(string errorMsg) :errorMsg{ errorMsg } {};
	string getErrorMessage() {
		return this->errorMsg;
	}
};

class TurismRepository {
private:
	vector<Turism> allTuristi;
public:
	TurismRepository() = default;
	//constructor de copiere
	TurismRepository(const TurismRepository& ot) = delete;
	// Adaugare locatie turism in lista
	void store(const Turism& t);
	
	//void modify(const Turism& t,int pret);
	void sterge(const Turism& t);
	
	//Returneaza lista cu toate locatile de turism 
	const vector<Turism>& getAllTurism();
	/*
	* Cauta o locatie de turism 
	* @param denumire: denumirea dupa care se cauta
	* @param destinatie:  destinatia dupa care se cauta
	* @param tip: tipul dupa care se cauta
	*/
	const Turism& find(string denumire, string destinatie, string tip);
	
	/*
	* Verifica daca tranzacita data exista in lista
	*/
	bool exists(const Turism& s);
};

void testeRepo();