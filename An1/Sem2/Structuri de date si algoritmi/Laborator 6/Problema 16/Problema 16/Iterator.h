#pragma once

#include "DO.h"

//using namespace std;

class Iterator{
	friend class DO;
private:
	//constructorul primeste o referinta catre Container
	//iteratorul va referi primul element din container
	Iterator(const DO& dictionar);

	//contine o referinta catre containerul pe care il itereaza
	const DO& dict;

	/* aici e reprezentarea specifica a iteratorului */

	//int curent;
	//void deplasare();

	vector<TElem> elems;
	std::vector <TElem>::iterator pozcrt;
	vector<TElem> interclasare(vector<TElem>v1, vector<TElem>v2, Relatie r);
public:

	//reseteaza pozitia iteratorului la inceputul containerului
	void prim();

	//muta iteratorul in container
	// arunca exceptie daca iteratorul nu e valid
	void urmator();

	//verifica daca iteratorul e valid (indica un element al containerului)
	bool valid() const;

	//returneaza valoarea elementului din container referit de iterator
	//arunca exceptie daca iteratorul nu e valid
	TElem element() const;
};

