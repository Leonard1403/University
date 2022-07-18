#include "Multime.h"
#include "IteratorMultime.h"
#include <iostream>

using namespace std;

//o posibila relatie
bool rel(TElem e1, TElem e2) {
	if (e1 <= e2) {
		return true;
	}
	else {
		return false;
	}
}

Nod::Nod(TElem e, PNod urm, PNod ant) {
	this->e = e;
	this->urm = urm;
	this->ant = ant;
}

TElem Nod::element() {
	return e;
}

PNod Nod::urmator() {
	return urm;
}

PNod Nod::anterior() {
	return ant;
}

Multime::Multime() {
	/* de adaugat */
	primul = nullptr;
	ultimul = nullptr;
}

void Multime::afisare()
{
	PNod copie = primul;
	while (copie != nullptr)
	{
		cout << copie->e << " ";
		copie = copie->urm;
	}
	cout << '\n';
}

//tetha(1) daca elementul adaugat se afla in capete sau tetha(n-1) unde n
//reprezinta nr de elemente

bool Multime::adauga(TElem elem) {
	/* de adaugat */
	//afisare();
	PNod q = new Nod(elem, nullptr, nullptr);
	//cout << "intrat in functie" << '\n';
	if (primul == nullptr)
	{
		//nu e nimic
		primul = q;
		ultimul = q;
		return true;
	}
	else if (rel(elem, primul->e) == true) {
		//relatie pentru primul element din lista
		if (primul->e == elem)
			return false;
		primul->ant = q;
		q->urm = primul;
		q->ant = nullptr;
		primul = q;
		return true;
	}
	else if (rel(ultimul->e, elem) == true) {
		if (ultimul->e == elem)
			return false;
		//relatie pentru ultimul element din lista
		ultimul->urm = q;
		q->ant = ultimul;
		q->urm = nullptr;
		ultimul = q;
		return true;
	}
	else
	{
		//cout << "intrat" << '\n';
		PNod copie = primul;
		while (copie != nullptr) {
			//cout << "Element curent: " << copie->e << '\n';
			//cout << "Elementul pe care dorim sa-l adaugam: " << elem << '\n';
			//cout << '\n';
			if (rel(elem, copie->e) == true) {
				if (copie->e == elem)
					return false;

				q->urm = copie;
				q->ant = copie->ant;
				copie->ant->urm = q;
				copie->ant = q;

				return true;
			}
			copie = copie->urm;
			/*
			if (rel(copie->e, elem) != true) {
				cout << "Comparare: " << copie->e << " " << elem << '\n';
				q->ant = copie->ant;
				q->urm = copie;
				if (copie->ant == nullptr)
					primul = q;
				copie->ant = q;
				return true;
			}
			copie = copie->urm;
			*/
		}
		/*
		ultimul->urm = q;
		q->ant = ultimul;
		q->urm = nullptr;
		ultimul = q;
		return true;
		*/
	}
	/*
	else {
		q->urm = primul;
		primul->ant = q;
		primul = q;
		return true;
	}
	*/
	return false;
}

void Multime::reuniune(const Multime& b) {
	PNod bPrim = b.primul;
	PNod copie = primul;
	while (bPrim != nullptr) {
		adauga(bPrim->e);
		bPrim = bPrim->urm;
	}
}
/* subgalgoritm reuniune(b)
* bPrim <- b.primul
* copie <- primul
* while(bPrim != nullptr)
*	adauga(bPrim->e)
*	bPrim <- bPrim->urm
*/

bool Multime::sterge(TElem elem) {
	/* de adaugat */
	// Θ(n) worst case scenario sau Θ(1) best case scenario
	PNod copie = primul;
	if (primul == nullptr)
		return false;
	else if (primul->urm == nullptr && primul->e==elem) {
		primul = primul->urm;
		ultimul = primul;
		copie->urm = nullptr;
		copie->ant = nullptr;
		delete copie;
		return true;
	}
	else if (primul->e == elem) {
		primul = primul->urm;
		primul->ant = nullptr;
		copie->urm = nullptr;
		copie->ant = nullptr;
		delete copie;
		return true;
	}
	else if (ultimul->e == elem) {
		copie = ultimul;
		ultimul = ultimul->ant;
		ultimul->urm = nullptr;
		copie->ant = nullptr;
		copie->urm = nullptr;
		delete copie;
		return true;
	}

	while (copie != nullptr) {
		if (copie->e == elem)
		{
			copie->urm->ant = copie->ant;
			copie->ant->urm = copie->urm;
			copie->urm = nullptr;
			copie->ant = nullptr;
			delete copie;
			return true;
		}
		copie = copie->urm;
	}
	return false;
}


bool Multime::cauta(TElem elem) const {
	/* de adaugat */
	// Θ(n) worst case scenario sau Θ(1) best case scenario
	PNod copie = primul;
	//cout << "Elementul cautat: " << elem << '\n';
	//cout << "copie: ";
	//cout << "intrat";
	while (copie != nullptr)
	{
		//cout << copie->e << " ";
		if (copie->e == elem) {
			return true;
		}
		copie = copie->urm;
	}
	//cout << '\n';
	return false;
}


int Multime::dim() const {
	/* de adaugat */
	PNod copie = primul;
	int dimensiune = 0;
	while (copie != nullptr) {
		copie = copie->urm;
		dimensiune = dimensiune + 1;
	}
	return dimensiune;;
}



bool Multime::vida() const {
	/* de adaugat */
	if (primul == nullptr)
		return true;
	return false;
}

IteratorMultime Multime::iterator() const {
	return IteratorMultime(*this);
}


Multime::~Multime() {
	while (primul != nullptr) {
		PNod p = primul;
		primul = primul->urm;
		delete p;
	}
	/* de adaugat */
}




