#pragma once
#include "MyList.h"
#include <string.h>
#include <assert.h>

MyList createEmpty() {
	MyList v;
	v.length = 0;
	return v;
}

void destroy(MyList* v) {
	v->length = 0;
}

ElemType get(MyList* v, int poz) {
	return v->elems[poz];
}

ElemType setElem(MyList* v, int poz, ElemType el) {
	ElemType replacedElement = v->elems[poz];
	v->elems[poz] = el;
	return replacedElement;
}


int size(MyList* v) {
	return v->length;
}

void add(MyList* v, ElemType el) {
	v->elems[v->length] = el;
	v->length++;
}

ElemType delete(MyList* v, int poz) {
	ElemType el = v->elems[poz];
	for (int i = poz; i < v->length - 1; i++) {
		v->elems[i] = v->elems[i + 1];
	}
	v->length--;
	return el;
}

MyList copyList(MyList* v) {
	MyList v_copy = createEmpty();
	for (int i = 0; i < v->length; i++) {
		ElemType el = get(v, i);
		add(&v_copy, el);
	}
	return v_copy;
}

void testCreateVector() {
	MyList v = createEmpty();
	//assert(v.length == 0);
	assert(size(&v) == 0);

}
void testIterate() {
	MyList v = createEmpty();
	Tranzactie m1 = createTranzactie(12,150,"intrare","Suma pentru alimentare");
	Tranzactie m2 = createTranzactie(8,50,"intrare","Flori");
	Tranzactie m3 = createTranzactie(21,2000,"iesire","Mancare");

	add(&v, m1);
	add(&v, m2);
	add(&v, m3);

	assert(size(&v) == 3);
	Tranzactie m = get(&v, 0);

	assert(m.ziua == 12);
	assert(m.suma == 150);
	assert(strcmp(m.tip,"intrare")==0);

	destroy(&v);
	assert(size(&v) == 0);

}

void testCopy() {
	MyList v1 = createEmpty();
	add(&v1, createTranzactie(12, 150, "intrare", "Suma pentru alimentare"));
	add(&v1, createTranzactie(21, 2000, "iesire", "Mancare"));

	assert(size(&v1) == 2);
	MyList v2 = copyList(&v1);
	assert(size(&v2) == 2);
	Tranzactie m = get(&v2, 0);
	assert(strcmp(m.descriere, "Suma pentru alimentare") == 0);

}

void testDelete(){
	MyList v1 = createEmpty();

	Tranzactie m1 = createTranzactie(12, 150, "intrare", "Suma pentru alimentare");
	Tranzactie m2 = createTranzactie(8, 50, "intrare", "Flori");
	Tranzactie m3 = createTranzactie(21, 2000, "iesire", "Mancare");
	add(&v1, m1);
	add(&v1, m2);
	add(&v1, m3);
	assert(size(&v1) == 3);

	Tranzactie m = delete(&v1, 2);


}