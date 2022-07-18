#include "Iterator.h"
#include "DO.h"
#include <iostream>
#include <cmath>
#include <exception>
#include <set>

using namespace std;

bool rel(TCheie e1, TCheie e2) {
	if (e1 <= e2)
		return true;
	else
		return false;
}

int hashCode(TValoare e) {
	return abs(e);
}

int DO::d(TCheie e) const{
	return hashCode(e) % m;
}

DO::DO(Relatie r) {
	m = MAX;
	n = 0;
	relatie = r;
	
	for (int i = 0; i < m; i++) {
		e[i].first = NULL_TVALOARE;
		e[i].second = NULL_TVALOARE;
		urm[i] = NULL_TVALOARE;
	}

	primLiber = 0;
	/* de adaugat */
}

void DO::actPrimLiber() {
	primLiber++;
	while (primLiber < m && e[primLiber].first != -1)
		primLiber++;
}

//adauga o pereche (cheie, valoare) in dictionar
//daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
//daca nu exista cheia, adauga perechea si returneaza null
TValoare DO::adauga(TCheie c, TValoare v) {
	/* de adaugat */

	/*
	int i = d(c);

	//std::cout << "Dispersia: " << i << '\n';

	if (e[i].first == -1) {
		//std::cout << "Intrat\n";
		e[i].first = c;
		e[i].second = v;
		if (i == primLiber) {
			//std::cout << "intrat cautare\n";
			actPrimLiber();
		}
		return NULL_TVALOARE;
	}
	else if (e[i].first == i) {
		int aux = e[i].second;
		e[i].second = v;
		return aux;
	}

	int j = -1;
	while (i != -1) {
		//std::cout << "Intrat in while\n";
		j = i;
		i = urm[i];
	}

	if (primLiber >= m)
		throw std::exception{ "Nu mai exista spatiu pentru adaugarea elementului" };

	e[primLiber].first = c;
	e[primLiber].second = v;

	urm[j] = primLiber;
	actPrimLiber();
	//std::cout << "primLiber: " << primLiber << '\n';

	return NULL_TVALOARE;
	*/

	TValoare val_veche = NULL_TVALOARE;
	int i = d(c), j, ok = 1, aux;
	if (e[i].first == NULL_TVALOARE) {
		e[i].first = c;
		e[i].second = v;
		if (i == primLiber)
			actPrimLiber();
		n++;
		return NULL_TVALOARE;
	}
	else {
		while (i != NULL_TVALOARE) {
			if ((Relatie)(c, e[i].first) && d(e[i].first) == i) {
				TCheie aux1 = c;
				TValoare aux2 = v;
				val_veche = e[i].second;
				c = e[i].first;
				v = e[i].second;
				e[i].first = aux1;
				e[i].second = aux2;

				e[primLiber].first = c;
				e[primLiber].second = v;
				urm[i] = primLiber;
				actPrimLiber();
				//n++;
				return val_veche;
			}
			j = i;
			i = urm[i];
		}
		e[primLiber].first = c;
		e[primLiber].second = v;
		urm[j] = primLiber;
		actPrimLiber();
		n++;
		return val_veche;
	}
}

//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null
TValoare DO::cauta(TCheie c) const {
	/* de adaugat */

	//for (int i = 0; i < m; i++)
	//	if (c == e[i].first)
	//		return e[i].second;
	//return NULL_TVALOARE;	
	
	int poz = d(c);
	vector<TValoare> v;
	while (poz != NULL_TVALOARE && e[poz].first != c) {
		poz = urm[poz];
	}

	while (poz != NULL_TVALOARE && e[poz].first == c)
	{
		v.push_back(e[poz].second);
		poz = urm[poz];
	}
	
	if (!v.size())
		return NULL_TVALOARE;
	else
		return v[0];

}

//sterge o cheie si returneaza valoarea asociata (daca exista) sau null

TValoare DO::sterge(TCheie c) {
	/* de adaugat */
	//int i = d(c);
	//if (e[i].first == -1)
	//	return NULL_TVALOARE;
	//else
	//{
	//	int aux = e[i].second;
	//	e[i].first = -1;
	//	e[i].second = -1;
	//	return aux;
	//}

	//return NULL_TVALOARE;

	int i = d(c), j = NULL_TVALOARE, k = 0, p, pp;

	bool gata;
	TValoare v;

	while (k < m && j == NULL_TVALOARE)
	{
		if (urm[k] == i) j = k;
		else k++;
	}
	v = e[i].second;
	TElem element(c, v);
	//cout << v << '\n';
	while (i != NULL_TVALOARE && e[i] != element) {
		j = i;
		i = urm[i];
	}

	if (i == NULL_TVALOARE)
	{
		return NULL_TVALOARE;
	}
	else {
		gata = false;
		do {
			p = urm[i];
			pp = i;
			while (p != NULL_TVALOARE && d(e[p].first) != i) {
				pp = p;
				p = urm[p];
			}
			if (p == NULL_TVALOARE)gata = true;
			else {
				e[i] = e[p];
				j = pp;
				i = p;
			}
		} while (!gata);
		if (j != NULL_TVALOARE)urm[j] = urm[i];
		e[i].first = NULL_TVALOARE;
		urm[i] = NULL_TVALOARE;
		if (primLiber > i) primLiber = i;
		n--;
		//return e[i].second;
	}
	return v;
}

//sterge o cheie si returneaza valoarea asociata (daca exista) sau null
//TValoare DO::sterge(TCheie c) {
//	TValoare v = sterge_da(c);
//	while (sterge_da(c) != NULL_TVALOARE);
//	return v;
//}

//returneaza numarul de perechi (cheie, valoare) din dictionar
int DO::dim() const {
	/* de adaugat */
	//int dimensiune = 0;
	//for (int i = 0; i < m; i++)
	//	if (e[i].first != -1)
	//		dimensiune++;
	//return dimensiune;
	return n;
}

//verifica daca dictionarul e vid
bool DO::vid() const {
	/* de adaugat */
	if(dim()==0)
		return true;
	return false;
}

//functionalitatea extra
//O(m^2)
/*
* frecventa <- 0
* ok <- 0
* frecventa_maxima <- 0
* pentru i<-0;i<m:
*	frecventa<-0
*	pentru j<-0;j<m:
*		daca e[i].second = e[j].second si e[i].second != -1
*			frecventa <- frecventa + 1
*	daca frecventa>frecventa_maxima
*		ok <- 1
*		frecventa_maxima <- frecventa
*		val <- e[i].second
*daca ok = 0
*	return NULL_TValoare
* else 
*	return val
*/
TValoare DO::ceaMaiFrecventaValoare() const {
	TValoare val;
	int frecventa = 0;
	bool ok = 0;
	int frecventa_maxima = 0;
	for (int i = 0; i < m; i++)
	{
		frecventa = 0;
		for (int j = 0; j < m; j++)
		{
			if (e[i].second == e[j].second&& e[i].second!=-1)
				frecventa++;
		}

		if(frecventa>frecventa_maxima)
		{ 
			ok = 1;
			frecventa_maxima = frecventa;
			val = e[i].second;
		}
	}
	if (ok == 0)
		return NULL_TVALOARE;
	else
		return val;
}

Iterator DO::iterator() const {
	return  Iterator(*this);
}

DO::~DO() {
	/* de adaugat */
}

void DO::afisare(TCheie c) {
	int i = d(c), j = NULL_TVALOARE, k = 0;
	while (k < m && j == NULL_TVALOARE)
	{
		if (urm[k] == i) j = k;
		else k++;
	}
	while (i != NULL_TVALOARE) {
		j = i;
		i = urm[i];
		cout << e[j].second << " ";
	}
	cout << '\n';
}