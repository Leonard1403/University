#include "Iterator.h"
#include "LO.h"

Iterator::Iterator(const LO& lo) : lo(lo){
	/* de adaugat */
	this->curent = lo.primul;
}

void Iterator::prim(){
	/* de adaugat */
	this->curent = lo.primul;
}

void Iterator::urmator(){
	/* de adaugat */
	this->curent = curent->urmator();
}

bool Iterator::valid() const{
	/* de adaugat */
	return curent != nullptr;
	//return false;
}

TElement Iterator::element() const{
	/* de adaugat */
	return curent->element();
	//return -1;
}


