#include "VectorDinamic.h"
#include "IteratorVectorDinamic.h"
#include <exception>

using namespace std;

}

}

VectorDinamic::~VectorDinamic() {
}

int VectorDinamic::dim() const{
	return 0;
}

TElem VectorDinamic::element(int i) const{
	return -1;
}

void VectorDinamic::adaugaSfarsit(TElem e) {
}

void VectorDinamic::adauga(int i, TElem e) {
}

TElem VectorDinamic::modifica(int i, TElem e) {
	/* de adaugat */
	return -1;
}

TElem VectorDinamic::sterge(int i) {
	return -1;
}
IteratorVectorDinamic VectorDinamic::iterator() {
}
