#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m): mult(m) {
	/* de adaugat */
	// Θ(1)
	this->curent = mult.primul;
}

TElem IteratorMultime::element() const {
	/* de adaugat */
	// Θ(1)
	return curent->element();
}

bool IteratorMultime::valid() const {
	/* de adaugat */
	// Θ(1)
	return curent != nullptr;
	//return false;
}

void IteratorMultime::urmator() {
	/* de adaugat */
	this->curent = curent->urmator();
}

void IteratorMultime::prim() {
	/* de adaugat */
	this->curent = mult.primul;
}

