#include "Iterator.h"
#include "LO.h"

#include <iostream>
using namespace std;

#include <exception>

Nod::Nod(TElement e, PNod urm, PNod ant) {
	this->e = e;
	this->urm = urm;
	this->ant = ant;
}

TElement Nod::element() {
	return e;
}

PNod Nod::urmator() {
	return urm;
}

PNod Nod::anterior() {
	return ant;
}

LO::LO(Relatie r) {
	/* de adaugat */
	primul = nullptr;
	ultimul = nullptr;
}

bool rel(TElement cheie1, TElement cheie2) {
	if (cheie1 <= cheie2) {
		return true;
	}
	else {
		return false;
	}
}
// returnare dimensiune
//returneaza numarul de perechi (cheie, valoare) din dictionar
int LO::dim() const {
	/* de adaugat */
	PNod copie = primul;
	int dimensiune = 0;
	while (copie != nullptr) {
		copie = copie->urm;
		dimensiune = dimensiune + 1;
	}
	return dimensiune;
}

// verifica daca LO e vida
bool LO::vida() const {
	if (primul == nullptr)
		return true;
	return false;
	/* de adaugat */
	//return true;
}

// prima pozitie din LO
Iterator LO::prim() const {
	/* de adaugat */
	Iterator it = Iterator(*this);
	it.curent = primul;
	return it;
}

// returnare element de pe pozitia curenta
//arunca exceptie daca poz nu e valid
TElement LO::element(Iterator poz) const {
	/* de adaugat */
	
	if (poz.valid() == true)
		return poz.curent->element();
	else {
		throw std::exception();
	}
}

//sterge element de pe o pozitie poz si returneaza elementul sters
//dupa stergere poz e pozitionat pe elementul de dupa cel sters
//arunca exceptie daca poz nu e valid
TElement LO::sterge(Iterator& poz) {
	/* de adaugat */
	PNod pozCurent = poz.curent;
	if (!poz.valid())
		throw std::exception();
	else if (pozCurent->urm == nullptr)
	{
		poz.curent = nullptr;
		delete pozCurent;
	}
	/*
	else if() {
		if (pozCurent->urm == nullptr)
		{
			pozCurent = nullptr;
			primul = nullptr;
			ultimul = nullptr;
		}
		else {
			pozCurent->urm->ant = pozCurent->ant;
			pozCurent->ant->urm = pozCurent->urm;
			pozCurent->urm = nullptr;
			pozCurent->ant = nullptr;
		}
		delete poz.curent;
		return 1;
	}
	*/
	return -1;
}


// cauta element si returneaza prima pozitie pe care apare (sau iterator invalid)
Iterator LO::cauta(TElement e) const{
	/* de adaugat */

	Iterator itr = Iterator(*this);
	itr.prim();
	PNod nodCurent = itr.curent;
	while (nodCurent!=nullptr) {
		if (e == nodCurent->e) {
			itr.curent = nodCurent;
			return itr;
		}
		nodCurent = nodCurent->urm;
	}
	itr.curent = nullptr;
	return itr;
	//return Iterator(*this);
}

// adaugare element in LO
void LO::adauga(TElement e) {
	/* de adaugat */
	PNod q = new Nod(e, nullptr, nullptr);
	
	if (primul == nullptr)
	{
		primul = q;
		ultimul = q;
	}
	else {
		q->urm = primul;
		primul->ant = q;
		primul = q;
	}
}

// muta elementul curent referit de iterator k pasi inainte, sau face iteratorul nevalid in cazul in care exista mai putin de k elemente ramase in lista.
// arunca exceptie in cazul in care iteratorul este nevalid sau in cazul in care k este zero sau negativ
void LO::avanseazaKPasi(int k) {
	if(dim()<=k)
		throw std::exception();
	while (k != 0)
	{
		Iterator itr = Iterator(*this);
		itr.urmator();
		k = k - 1;
	}
}
//destructor
LO::~LO() {
	/* de adaugat */
	while (primul != nullptr) {
		PNod p = primul;
		primul = primul->urm;
		delete p;
	}
}
