#include "IteratorMultime.h"
#include "Multime.h"


IteratorMultime::IteratorMultime(const Multime& m) : multime(m){
	/* de adaugat */
	curent = 0;
}


void IteratorMultime::prim() {
	/* de adaugat */
	curent = 0;
}


void IteratorMultime::urmator() {
	/* de adaugat */
	curent++;
}


TElem IteratorMultime::element() const {
	/* de adaugat */
	return multime.e[curent];
}

bool IteratorMultime::valid() const {
	/* de adaugat */
	return curent < multime.dim();
}
