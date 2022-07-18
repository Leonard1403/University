#include <exception>
#include <iostream>
#include "LI.h"
#include "IteratorLI.h"

int LI::aloca() {
	//ok
	int i = primLiber;
	primLiber = urm[primLiber];
	ant[primLiber] = 0;
	return i;
}

void LI::dealoca(int i) {
	//ok
	ant[primLiber] = i;
	urm[i] = primLiber;
	primLiber = i;
	ant[primLiber] = 0;

	e[primLiber] = -1;
}

void LI::initSpatiuLiber() {
	//ok
	for (int i = 1; i <= cp - 1; i++) {
		urm[i] = i + 1;
	}
	urm[cp] = 0;
	primLiber = 1;
}

void LI::redim() {
	//ok
	//Θ(n)
	TElem* enou = new TElem[2 * cp];
	int* unou = new int[2 * cp];
	int* pnou = new int[2 * cp];

	for (int i = 1; i <= lg; i++) {
		enou[i] = e[i];
		unou[i] = urm[i];
		pnou[i] = ant[i];
	}

	cp *= 2;
	delete[] e;
	delete[] urm;
	delete[] ant;

	e = enou;
	urm = unou;
	ant = pnou;
	primLiber = lg + 1;
	for (int i = lg + 1; i < cp; i++) {
		urm[i] = i + 1;
		ant[i] = i - 1;
	}
	urm[cp] = 0;

	ant[cp] = cp - 1;
	ant[primLiber] = 0;
}

int LI::creeazaNod(TElem v) {
	//ok
	if (primLiber == 0) {
		redim();
	}
	int i = aloca();
	e[i] = v;
	urm[i] = 0;
	ant[i] = 0;
	return i;
}

LI::LI() {
	/* de adaugat */
	//ok
	cp = 1;
	primLiber = 0;

	e = new TElem[cp];
	urm = new int[cp];
	ant = new int[cp];
	lg = 0;

	initSpatiuLiber();
	prim = 0;
	ultim = 0;
}

int LI::dim() const {
 	/* de adaugat */
	//ok
	return lg;
}


bool LI::vida() const {
	/* de adaugat */
	//ok
	return prim == 0;
}

TElem LI::element(int i) const {
	/* de adaugat */
	return -1;
}

TElem LI::modifica(int i, TElem e) {
	/* de adaugat */
	return -1;
}

void LI::adaugaSfarsit(TElem e) {
	/* de adaugat */
}

void LI::adauga(int i, TElem elem) {
	/* de adaugat */
	//ok
	int nou = creeazaNod(elem);
	if (i > lg) {
		throw std::exception();
	}
}

TElem LI::sterge(int i) {
	/* de adaugat */
	return 0;
}

int LI::cauta(TElem element) const{
	/* de adaugat */
	//ok
	int crt = prim;
	while (crt != 0) {
		if (e[crt] == element) {
			return crt;
		}
		crt = urm[crt];
	}

	return -1;
}

IteratorLI LI::iterator() const {
	return  IteratorLI(*this);
}

LI::~LI() {
	/* de adaugat */
	//ok
	delete[] e;
	delete[] urm;
	delete[] ant;
}
