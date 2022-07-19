#include "Turism.h"
#include <assert.h>
#include <iostream>

string Turism::getDenumire() const {
	return this->denumire;
}

string Turism::getDestinatie() const {
	return this->destinatie;
}
string Turism::getTip() const {
	return this->tip;
}

int Turism::getPret() const {
	return this->pret;
}

void Turism::setDenumire(string denumireNOU) {
	this->denumire = denumireNOU;
}
void Turism::setDestinatie(string destinatieNOU) {
	this->destinatie = destinatieNOU;
}

void Turism::setTip(string tipNOU) {
	this->tip = tipNOU;
}

void Turism::setPret(int pretNOU) {
	this->pret = pretNOU;
}

bool cmpDenumire(const Turism& m1, const Turism& m2) {
	return m1.getDenumire() < m2.getDenumire();
}

bool cmpDestinatie(const Turism& m1, const Turism& m2) {
	return m1.getDestinatie() < m2.getDestinatie();
}

bool cmpTipAndPret(const Turism& m1, const Turism& m2) {
	if (m1.getTip() == m2.getTip())
		return m1.getPret() < m2.getPret();
	else
		return m1.getTip() < m2.getTip();
}

void testGetSet() {
	/*
	* string denumire;
	string destinatie;
	string tip;
	int pret;
	*/
	Turism turism1{ "La munte","Sinaia","munte",200 };
	Turism turism2{ "munte","inaia","te",20 };
	Turism turism3{ "munte","inaia","da",400 };
	Turism turism4{ "mare","malayeye","da",20 };

	cmpTipAndPret(turism1, turism2);
	cmpTipAndPret(turism2, turism1);
	cmpTipAndPret(turism2, turism3);
	cmpTipAndPret(turism4, turism3);

	cmpDestinatie(turism1, turism2);
	cmpDestinatie(turism2, turism1);

	cmpDenumire(turism1, turism2);
	cmpDenumire(turism2, turism1);

	//std::cout << turism1.getDenumire() << " " << turism1.getDestinatie() << " " << turism1.getTip() << " " << turism1.getPret() << '\n';
	assert(turism1.getDenumire() == "La munte");
	assert(turism1.getDestinatie() == "Sinaia");
	assert(turism1.getPret() == 200);
	assert(turism1.getTip() == "munte");
	
	turism1.setDenumire("La mare");
	turism1.setDestinatie("Constanta");
	turism1.setPret(100);
	turism1.setTip("mare");

	assert(turism1.getDenumire() == "La mare");
	assert(turism1.getDestinatie() == "Constanta");
	assert(turism1.getPret() == 100);
	assert(turism1.getTip() == "mare");

}

void testeDomain() {
	testGetSet();
}