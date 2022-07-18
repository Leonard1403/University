#pragma once

class Iterator;

typedef int TComparabil;
typedef TComparabil TElement;

typedef bool (*Relatie)(TElement, TElement);

#define NULL_TELEMENT -1

class Nod;
class LO;

typedef Nod* PNod;


bool rel(TElement e1, TElement e2);

class Nod {
public: 
	friend class LO;
	
	Nod(TElement, PNod urm, PNod ant);
	TElement element();
	PNod urmator();
	PNod anterior();
private:

	TElement e;
	PNod urm;
	PNod ant;
};



class LO {
private:
	friend class Iterator;
private:
	/* aici reprezentarea */
	PNod primul, ultimul;
public:
		// constructor
		LO (Relatie r);

		// returnare dimensiune
		int dim() const;

		// verifica daca LO e vida
		bool vida() const;

		// prima pozitie din LO
		Iterator prim() const;

		// returnare element de pe pozitia curenta
		//arunca exceptie daca poz nu e valid
		TElement element(Iterator poz) const;

		// adaugare element in LO a.i. sa se pastreze ordinea intre elemente
		void adauga(TElement e);

		// sterge element de pe o pozitie poz si returneaza elementul sters
		//dupa stergere poz e pozitionat pe elementul de dupa cel sters
		//arunca exceptie daca poz nu e valid
		TElement sterge(Iterator& poz);

		// cauta element si returneaza prima pozitie pe care apare (sau iterator invalid)
		Iterator cauta(TElement e) const;

		// muta elementul curent referit de iterator k pasi inainte, sau face iteratorul nevalid in cazul in care exista mai putin de k elemente ramase in lista.
		// arunca exceptie in cazul in care iteratorul este nevalid sau in cazul in care k este zero sau negativ
		void avanseazaKPasi(int k);

		//destructor
		~LO();

};
