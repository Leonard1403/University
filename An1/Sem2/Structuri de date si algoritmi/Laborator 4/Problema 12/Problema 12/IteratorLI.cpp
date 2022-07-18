#include "IteratorLI.h"
#include "LI.h"
#include <exception>

IteratorLI::IteratorLI(const LI& li): lista(li) {
 	/* de adaugat */
    //ok
    curent = li.prim;
}

void IteratorLI::prim(){
 	/* de adaugat */
    //ok
    curent = lista.prim;
}

void IteratorLI::urmator(){
 	/* de adaugat */
    //ok
    if (valid()) {
        curent = lista.urm[curent];
    }
    else {
        throw 1;
    }
}

void IteratorLI::anterior() {
    //ok
    if (valid()) {
        curent = lista.ant[curent];
    }
    else {
        throw 1;
    }
}

bool IteratorLI::valid() const{
 	/* de adaugat */
    //ok
    int i = lista.prim;
    while (i != 0) {
        if (i == curent) {
            return true;
        }
        i = lista.urm[i];
    }
    return false;
}

TElem IteratorLI::element() const{
 	/* de adaugat */
    //ok
    if (valid())
        return lista.e[curent];
    throw 1;
}
