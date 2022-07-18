#pragma once
#include "Turism.h"
#include <vector>

using std::vector;
using std::unique_ptr;

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
	//TurismRepository() = default;
	TurismRepository() {
		vector <Turism> lst;
		allTuristi = lst;
	}
	
	//constructor de copiere
	TurismRepository(const TurismRepository& ot) = delete;
	// Adaugare locatie turism in lista
	virtual void store(const Turism& t);
	
	//void modify(const Turism& t,int pret);
	virtual void sterge(Turism& t);

	virtual void modify(Turism& t);
	
	//Returneaza lista cu toate locatile de turism 
	virtual const vector<Turism>& getAllTurism();
	/*
	* Cauta o locatie de turism 
	* @param denumire: denumirea dupa care se cauta
	* @param destinatie:  destinatia dupa care se cauta
	* @param tip: tipul dupa care se cauta
	*/
	const Turism& find(string denumire);
	
	//functie care returneaza dimensiunea listei de destinatii 
	size_t get_dim();

	/*
	* Verifica daca tranzacita data exista in lista
	*/
	bool exists(const Turism& s);
};

class TurismRepositoryFile :public TurismRepository {
private:
	std::string fileName;

	//Extragem activitatile din fisier
	void loadFromFile();

	//Salveaza lista curenta de activitati in fisier
	void saveToFile();
public:
	TurismRepositoryFile(std::string fileName) :TurismRepository(), fileName{ fileName }{
		loadFromFile();
	}

	void store(const Turism& a) override;

	void sterge(Turism& a) override;

	void modify(Turism& a) override;

};


void testeRepo();
void test_resize();