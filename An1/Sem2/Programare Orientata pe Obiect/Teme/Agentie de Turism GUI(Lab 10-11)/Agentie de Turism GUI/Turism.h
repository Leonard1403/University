#pragma once
#include <string>
#include <iostream>

using std::string;
using std::cout;
using std::endl;

class Turism {
private:
	string denumire;
	string destinatie;
	string tip;
	int pret;
public:
	Turism() = delete;
	Turism(string denumire, string destinatie, string tip, int pret) :denumire{ denumire }, destinatie{ destinatie }, tip{ tip }, pret{ pret }{};
	Turism(const Turism& ot) :denumire{ ot.denumire }, destinatie{ ot.destinatie }, tip{ ot.tip }, pret{ ot.pret }{
		//cout << "[TURISM] Constructor de copiere" << endl;
	}
	string getDenumire() const;
	string getDestinatie() const;
	string getTip() const;
	int	   getPret() const;

	void setDenumire(string denumireNOU);
	void setDestinatie(string destinatieNOU);
	void setTip(string tipNOU);
	void setPret(int pretNOU);

	bool eq(Turism a);
};

bool cmpDenumire(const Turism& m1, const Turism& m2);

bool cmpDestinatie(const Turism& m1, const Turism& m2);

bool cmpTipAndPret(const Turism& m1, const Turism& m2);

void testeDomain();