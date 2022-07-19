#include "Repository.h"
#include <assert.h>

bool TurismRepository::exists(const Turism& s) {
	try {
		//string denumire, string destinatie, string tip
		find(s.getDenumire(), s.getDestinatie(), s.getTip());
		return true;
	}
	catch (RepoException) {
		return false;
	}
}

const Turism& TurismRepository::find(string denumire, string destinatie, string tip) {
	for (const Turism& s : this->allTuristi) {
		if (s.getDenumire() == denumire && s.getDestinatie() == destinatie && s.getTip() == tip) {
			return s;
		}
	}
	//std::cout << "Locatia de turism cu Denumirea: " + denumire + " Destinatia " + destinatie + " si Tipul " + tip + " nu se afla in lista\n";
	throw RepoException("Locatia de turism cu Denumirea: " + denumire + " Destinatia " + destinatie + " si Tipul " + tip + " nu se afla in lista");
}

void TurismRepository::store(const Turism& s) {
	if (exists(s)) {
		/*
		* string getDenumire() const;
		* string getDestinatie() const;
		* string getTip() const;
		* int	   getPret() const;
		*/
		// find(s.getDestinatie(), s.getTip());
		//std::cout << "Locatia de turism  cu Destinatia: " + s.getDestinatie() + " si Tipul: " + s.getTip() + " exista deja\n";
		throw RepoException("Locatia de turism  cu Destinatia: "  + s.getDestinatie() + " si Tipul: " + s.getTip() + " exista deja");
	}
	this->allTuristi.push_back(s);
}

void TurismRepository::sterge(const Turism& s) {
	bool ok = 0;
	for (int i = 0; i < allTuristi.size()-1; i++) {
		//string denumire;
		//string destinatie;
		//string tip;
		//int pret;
		if (allTuristi[i].getDenumire() == s.getDenumire() && allTuristi[i].getDestinatie() == s.getDestinatie() && allTuristi[i].getTip() == s.getTip() && allTuristi[i].getPret() == s.getPret())
		{
			ok = 1;
		}
		if (ok == 1) {
			allTuristi[i] = allTuristi[i + 1];
		}
	}
	this->allTuristi.pop_back();
}
/*
void TurismRepository::modify(const Turism& t,int pret) {

}
void TurismRepository::sterge(const Turism& t) {

}
*/

const VectorDinamic<Turism>& TurismRepository::getAllTurism() {
	return this->allTuristi;
}

void testAddRepo() {
	TurismRepository testRepo;
	//string denumire, string destinatie, string tip, int pret
	Turism turism1{"La prapastia din vale","Floresti","munte",200};
	testRepo.store(turism1);

	VectorDinamic < Turism > allTuristi = testRepo.getAllTurism();
	assert(allTuristi.size() == 1);

	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "La prapastia din vale","Floresti","munte",9800 };
	//testRepo.store(turism3);
	try {
		testRepo.store(turism3);
		//modif ->
		//assert(false);
	}
	catch (RepoException) {
		assert(true);
	}
}

void testFindRepo() {
	//
	TurismRepository testRepo;
	Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "In campul de lalele","Cluj-Napoca","deal",9800 };

	testRepo.store(turism1);
	testRepo.store(turism2);

	assert(testRepo.exists(turism1));
	assert(!testRepo.exists(turism3));

	auto foundTurism = testRepo.find("La prapastia din vale", "Floresti", "munte");
	assert(foundTurism.getDenumire() == "La prapastia din vale");
	assert(foundTurism.getDestinatie() == "Floresti");
	assert(foundTurism.getPret() == 200);
	assert(foundTurism.getTip() == "munte");

	try {
		testRepo.find("nowhere", "no", "where");
		//modif ->
		//assert(false);
	}
	catch (RepoException& ve) {
		assert(ve.getErrorMessage() == "Locatia de turism cu Denumirea: nowhere Destinatia no si Tipul where nu se afla in lista");
	}
}

void testStergeRepo() {
	TurismRepository testRepo;
	Turism turism1{ "La prapastia din vale","Floresti","munte",200 };
	Turism turism2{ "La Veriku","Cluj-Napoca","atelier auto",500 };
	Turism turism3{ "In campul de lalele","Cluj-Napoca","deal",9800 };
	testRepo.store(turism1);
	testRepo.store(turism2);
	testRepo.store(turism3);
	
	testRepo.sterge(turism1);
	try {
		testRepo.find("La prapastia din vale", "Floresti", "munte");
		//modif ->
		//assert(false);
	}
	catch (RepoException& ve) {
		assert(ve.getErrorMessage() == "Locatia de turism cu Denumirea: La prapastia din vale Destinatia Floresti si Tipul munte nu se afla in lista");
	}
}

void testeRepo() {
	testAddRepo();
	testFindRepo();
	testStergeRepo();
}