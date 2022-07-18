#pragma once
#include <vector>

#define MAX 400

typedef int TCheie;
typedef int TValoare;

#define NULL_TVALOARE -1

#include <utility>
typedef std::pair<TCheie, TValoare> TElem;
//first -> cheia || second -> valoarea
class Iterator;

typedef bool(*Relatie)(TCheie, TCheie);
//bool rel(TCheie, TCheie);

using namespace std;

class DO {
	friend class Iterator;
    private:
	/* aici e reprezentarea */
	
	int n;
	int m; //numarul de locatii din tabela de dispersie
	TElem e[MAX]; //vectorul elementelor - vector static
	int urm[MAX]; //vectorul legaturilor
	int primLiber; //locatia primei pozitii libere din tabela
	
	//actualizare primLiber
	void actPrimLiber();
	//functia de dispersie
	int d(TCheie e) const;

    public:

	Relatie relatie;
	// constructorul implicit al dictionarului
	DO(Relatie r);


	// adauga o pereche (cheie, valoare) in dictionar
	//daca exista deja cheia in dictionar, inlocuieste valoarea asociata cheii si returneaza vechea valoare
	// daca nu exista cheia, adauga perechea si returneaza null: NULL_TVALOARE
	TValoare adauga(TCheie c, TValoare v);

	//cauta o cheie si returneaza valoarea asociata (daca dictionarul contine cheia) sau null: NULL_TVALOARE
	TValoare cauta(TCheie c) const;


	//sterge o cheie si returneaza valoarea asociata (daca exista) sau null: NULL_TVALOARE
	TValoare sterge_da(TCheie c);
	TValoare sterge(TCheie c);

	//returneaza numarul de perechi (cheie, valoare) din dictionar
	int dim() const;

	//verifica daca dictionarul e vid
	bool vid() const;

	void afisare(TCheie c);
	// se returneaza iterator pe dictionar
	// iteratorul va returna perechile in ordine dupa relatia de ordine (pe cheie)
	Iterator iterator() const;

	//Functionalitate noua
	TValoare ceaMaiFrecventaValoare() const;

	// destructorul dictionarului
	~DO();

};
