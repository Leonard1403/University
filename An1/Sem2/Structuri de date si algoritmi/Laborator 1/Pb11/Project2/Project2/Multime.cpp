#include "Multime.h"
#include "IteratorMultime.h"

#include <iostream>


void Multime::redim() {
	TElem *eNou = new int[2 * cp];

	for (int i = 0; i < n; i++)
		eNou[i] = e[i];

	cp = 2 * cp;

	delete[] e;

	e = eNou;
}

Multime::Multime() {
	/* de adaugat */
	this->cp = 1;
	e = new TElem[1];

	this->n = 0;
}


bool Multime::adauga(TElem elem) {
	/* de adaugat */
	if (n == cp)
		redim();
	for (int i = 0; i < n; i++)
	{
		if (this->e[i] == elem)
			return false;
	}

	this->e[n++] = elem;
	return true;
}


bool Multime::sterge(TElem elem) {
	/* de adaugat */
	int poz = -1;
	int nNou = 0;
	//std::cout << "n normal: " << this->n << '\n';
	for (int i = 0; i < n; i++)
	{
		if (this->e[i] == elem) {
			poz = i;
			break;
		}
	}
	if(poz==-1)
		return false;
	else
	{
		TElem* eNou = new int[cp];

		for (int i = 0; i < n; i++)
		{
			if (poz != i) {
				eNou[nNou++] = e[i];
			}
		}
		delete[] e;

		e = eNou;
		this->n = nNou;
		n = nNou;
		//std::cout << "n nou: " << nNou << '\n';
		return true;
	}
}


bool Multime::cauta(TElem elem) const {
	/* de adaugat */
	for (int i = 0; i < n; i++)
	{
		if (this->e[i] == elem)
			return true;
	}
	return false;
}


int Multime::dim() const {
	/* de adaugat */
	return n;
}

bool Multime::vida() const {
	/* de adaugat */
	if(this->n == 0)
		return true;
	return false;
}


Multime::~Multime() {
	/* de adaugat */
	delete[] e;
}



IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}

